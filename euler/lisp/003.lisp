;;;; Project Euler: an exercise in inductive chain learning
;;;; Problem 3: Largest prime factor

;;; The prime factors of 13195 are 5, 7, 13 and 29.
;;;
;;; What is the largest prime factor of the number 600851475143?


;;; Helper functions

(defun is-prime (num)
  ;; Yields whether the only factors of a given number /num/ are 1 and itself:
  (equalp (list 1 num)
          (remove-if-not (lambda (x)
                                 (is-factor-of num x))
                         (range 1 (+ num 1)))))

;; This would appear to be the first problem requiring some measure of real
;; optimization. The function looks tidy and works as expected for small
;; numbers, but there is a problem:

(print (is-prime 30000000))             ; takes 5-7 seconds, larger numbers
;; : NIL                                ; take exponentially longer

;; Instead of iterating over the entire range of 1 < x < /num/ every time we
e, we have to find a better way. The pattern from the
;; Fibonacci function used in a prior problem might work here:

(defun prime-factors (num)
  (defun prime-acc (dividend divisor divisors)
    ;; given a dividend, divisor, and sequence of divisors,
    (let ((quotient (/ dividend divisor)))
         (cond
             ;; if the quotient is 1, return divisors
             ((equal quotient 1) (adjoin divisor divisors))

             ;; if the quotient is an integer, adjoin divisor and rerun
             ((integerp quotient)
               (prime-acc quotient divisor (adjoin divisor divisors)))

             ;; otherwise increment divisor and rerun
             (T (prime-acc dividend (+ 1 divisor) divisors)))))

  ;; Reverse output of accumulator
  (reverse (prime-acc num 2 nil)))

;; This works by passing /num/ to *prime-acc* as /dividend/, which is divided
;; successively (at first by 2, passed as /divisor/). If the quotient is a
;; whole number, /divisor/ is appended to /divisors/ (at first an empty list)
;; and *prime-acc* is rerun with the quotient as its new /dividend/. When
;; *prime-acc* encounters a non-whole quotient, /divisor/ is incremented and
;; the function is rerun.

;; The call to *reverse* at the end of the main function is because we're
;; using *adjoin* instead of *append*. *adjoin* causes the function to treat
;; /divisors/ as a set and thereby return only one instance of each prime
;; factor--and necessitates the reversal--but the function could be easily
;; adapted to identify primes in a similar way by checking if /divisor/ is
;; already a member of /divisors/.


;;; Tests

;; Everything looks good:

(print (prime-factors 10))
;; : (2 5)

(print (prime-factors 190))
;; : (2 5 19)

(print (prime-factors 1902))
;; : (2 3 317)

(print (prime-factors 256))
;; : (2)

(print (prime-factors 13195))
;; : (5 7 13 29)


;;; Solution

;; Now let's try using *prime-factors* to find the largest prime factor of 600851475143:

(print (last (prime-factors 600851475143)))
;; : (6857)

;; Nice and quick!