package main

import (
	"errors"
	"fmt"
	"time"
)

// a typical example of errror return values.
func add3(arg int) (int, error) {
	if arg == 42 {
		return -1, errors.New("can't work with 42")
	}

	return arg + 3, nil
}

// a custom error type
type argError struct {
	arg  int
	prob string
}

func (e *argError) Error() string {
	return fmt.Sprintf("%d - %s", e.arg, e.prob)
}

// remade with custom error
func add3CustomError(arg int) (int, error) {
	if arg == 42 {
		return -1, &argError{arg, "can't work with it."}
	}

	return arg + 3, nil
}

// a nice little goroutine.
func prtRoutine(from string) {
	for i := 0; i < 3; i++ {
		fmt.Println(from, ":", i)
	}
}

// func only accepts a channel for sending values.
func ping(pings chan<- string, msg string) {
	pings <- msg
}

// func accepts 1 channel for receives, and another for sends.
func pong(pings <-chan string, pongs chan<- string) {
	msg := <-pings
	pongs <- msg
}

// another cute goroutine
func worker(done chan bool) {
	fmt.Print("working....")
	time.Sleep(time.Second)
	fmt.Println("done")

	done <- true // sned a value to notify another goroutine we're done.
}

func main() {
	/*
	   In Go it’s idiomatic to communicate errors via an explicit, separate return
	   value. This contrasts with the exceptions used in languages like Java and
	   Ruby and the overloaded single result / error value sometimes used in C.
	   Go’s approach makes it easy to see which functions return errors and to
	   handle them using the same language constructs employed for any other,
	   non-error tasks.
	*/
	for _, i := range []int{7, 42} {
		if r, e := add3(i); e != nil { // inline error check is a common Go idiom.
			fmt.Println("f1 failed:", e)
		} else {
			fmt.Println("f1 worked:", r)
		}
	}

	for _, i := range []int{7, 42} {
		if r, e := add3CustomError(i); e != nil {
			fmt.Println("f2 failed:", e)
		} else {
			fmt.Println("f2 worked:", r)
		}
	}

	_, e := add3CustomError(42)
	if ae, ok := e.(*argError); ok {
		fmt.Println(ae.arg)
		fmt.Println(ae.prob)
	}

	/*
	   A goroutine is a lightweight thread of execution.
	*/

	// suppose we have a function call f(s).
	// Here's how we'd call that in the usual way, running it synchronously.
	prtRoutine("direct")

	// to invoke this same function in a goroutine, use go f(s)
	// this new goroutine will execute concurrently with the calling one.
	go prtRoutine("goroutine")

	// you can also start a goroutine for an anonymous function call.
	go func(msg string) {
		fmt.Println(msg)
	}("going")

	// now the 2 func calls are running asynch. in separate goroutines now
	// so execution falls through to here.
	// This Scanln code requires we press a key before the program exits.
	var input string
	fmt.Scanln(&input)
	fmt.Println("done")

	/*
	   Channels are the pipes that connect concurrent goroutines. You can send
	   values into channels from one goroutine and receive those values into
	   another goroutine.
	*/

	// channels are typed by the values they convey
	messages := make(chan string) // create a new channel with make(chan val-type)

	// send a value into a channel using the channel <- syntax.
	go func() { messages <- "ping" }()

	msg := <-messages // <- channel syntax recieves a value from the channel.
	fmt.Println(msg)
	// by default sends and receives block until both the sender and receiver are
	// ready. This property allows us to wait at the end of our program for the
	// ping message.

	/*
	   By default channels are unbuffered, meaning that they will only accept
	   sends (chan <-) if there is a corresponding receive (<- chan) ready to
	   receive the sent value. Buffered channels accept a limited number of
	   values without a corresponding receiver for those values.
	*/

	// create a channel of strings buffered up to 2 values.
	messages2 := make(chan string, 2)

	// because messages2 is buffered, we can send these values into the channel
	// without a corresponding concurrent receive
	messages2 <- "buffered"
	messages2 <- "channel"

	fmt.Println(<-messages2)
	fmt.Println(<-messages2)

	/*
	   We can use channels to synchronize execution across goroutines. Here’s an
	   example of using a blocking receive to wait for a goroutine to finish.
	*/

	done := make(chan bool, 1)
	go worker(done) // start worker goroutine, giving it the channel to notify.

	<-done // block until we receive a notifcation from the worker on the chnl.

	/*
	   When using channels as function parameters, you can specify if a channel
	   is meant to only send or receive values. This specificity increases the
	   type-safety of the program.
	*/

	pings := make(chan string, 1)
	pongs := make(chan string, 1)
	ping(pings, "passed message")
	pong(pings, pongs)
	fmt.Println(<-pongs)

	/*
	   Go’s select lets you wait on multiple channel operations. Combining
	   goroutines and channels with select is a powerful feature of Go.
	*/
	chan1 := make(chan string)
	chan2 := make(chan string)

	go func() {
		time.Sleep(time.Second * 1)
		chan1 <- "one"
	}()

	go func() {
		time.Sleep(time.Second * 2)
		chan2 <- "two"
	}()

	// We'll use select to await both of these values simultaneously.
	for i := 0; i < 2; i++ {
		select {
		case msg1 := <-chan1:
			fmt.Println("received", msg1)
		case msg2 := <-chan2:
			fmt.Println("received", msg2)
		}
	}

	/*
	   Timeouts are important for programs that connect to external resources or
	   that otherwise need to bound execution time. Implementing timeouts in Go
	   is easy and elegant thanks to channels and select.
	*/

	// eg. suppose we're executing an external call that returns its result on a
	// channel chan3 after 2s.
	chan3 := make(chan string, 1)
	go func() {
		time.Sleep(time.Second * 2)
		chan3 <- "result 1"
	}()

	// Here the select implements a timeout.
	// res := <-chan3 awaits the result and <-Time.After awaits a value to be sent
	// after the timeout of 1s.
	// since select proceeds with the first receive that's ready, we'll take the
	// timeout case if the operation takes more than the allowed 1s.
	select {
	case res := <-chan3:
		fmt.Println(res)
	case <-time.After(time.Second * 1):
		fmt.Println("timeout 1")
	}

	chan4 := make(chan string, 1)
	go func() {
		time.Sleep(time.Second * 2)
		chan4 <- "result 2"
	}()

	// if we allow a longer timeout of 3s, then the receive from chan2
	// will succeed and we'll print the result.
	select {
	case res := <-chan4:
		fmt.Println(res)
	case <-time.After(time.Second * 3):
		fmt.Println("timeout 2")
	}

	/*
	   Basic sends and receives on channels are blocking. However, we can use
	   select with a default clause to implement non-blocking sends, receives,
	   and even non-blocking multi-way selects.
	*/
	messages = make(chan string)
	signals := make(chan bool)

	// a non blocking receive. If a value is avail. on messages then select will
	// take the messages case with that value.
	// else, immediately take default case.
	select {
	case msg := <-messages:
		fmt.Println("received message", msg)
	default:
		fmt.Println("no message received")
	}

	// a non blocking send works similarly
	msg = "hi"
	select {
	case messages <- msg:
		fmt.Println("sent message", msg)
	default:
		fmt.Println("no message sent")
	}

	// we can use multiple cases above the default to implement a multi-way
	// non-blocking select.
	select {
	case msg := <-messages:
		fmt.Println("received message", msg)
	case sig := <-signals:
		fmt.Println("received signal", sig)
	default:
		fmt.Println("no activity.")
	}

	/*
	   Closing a channel indicates that no more values will be sent on it.
	   This can be useful to communicate completion to the channel's receivers.
	*/

	// communicates work to be done from the main() goroutine to a wrker goroutine
	jobs := make(chan int, 5)
	done = make(chan bool)

	go func() {
		for {
			// in this special 2val form, more will be false if job is closed
			j, more := <-jobs
			if more {
				fmt.Println("received job", j)
			} else {
				fmt.Println("received all jobs")
				done <- true
				return
			}
		}
	}()

	for j := 1; j <= 3; j++ { // sends 3 jobs to the worker over the channel.
		jobs <- j
		fmt.Println("sent job", j)
		time.Sleep(3)
	}
	close(jobs)
	fmt.Println("sent all jobs")

	<-done // await worker using the synchronization approach we used earlier.
}
