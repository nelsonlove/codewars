;;;; Project Euler: an exercise in inductive chain learning
;;;; Problem 1: Multiples of 3 and 5

;;; If we list all the natural numbers below 10 that are multiples of 3 or 5,
;;; we get 3, 5, 6 and 9. The sum of these multiples is 23.
;;;
;;; Find the sum of all the multiples of 3 or 5 below 1000.


;;; Helper functions

(defun is-factor-of (num x)
  ;; Returns true if x ÷ y yields an integer.
  (integerp (/ num x)))

(defun range (min max)
  ;; Evals to a list of integers /min/ to /max/ exclusive:
  (loop for n from min below max by 1 collect n))

(defun sum (numbers)
  ;; Takes a list of numbers as input and passes it as
  ;; args to LISP's addition function. Removes nil elements
  ;; from input list:
  (apply '+ (remove nil numbers)))


;;; Tests

(print (is-factor-of 100 25))
;; : T
(print (is-factor-of 100 23))
;; : NIL
(print (range 1 10))
;; : (1 2 3 4 5 6 7 8 9)
(print (sum '(1 2 3 nil 4)))
;; : 10


;;; Solution

(defun sum-of-multiples (max &rest factors)
  ;; From a range of numbers from 1 to an upper limit given by /max/, yield
  ;; the sum of the numbers which have one or more given /factors/:
  (sum (remove-if-not (lambda (num)
                               (some (lambda (factor)
                                             (is-factor-of num factor))
                                     factors))
                       (range 1 max))))

(print (sum-of-multiples 1000 3 5))
;; : 233168
