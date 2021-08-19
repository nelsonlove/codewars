;;;; Project Euler: an exercise in inductive chain learning
;;;; Problem 6: Sum square difference

;;; The sum of the squares of the first ten natural numbers is:
;;;
;;; 1^2 + 2^2 + [...] + 10^2 = 385
;;;
;;; Hence the difference between the sum of the squares of the first ten
;;; natural numbers and the square of the sum is:
;;;
;;; sum(1...10) = 55
;;; sum(1...10)^2 = 55^2 = 3025
;;; 3025 - 385 = 2640
;;;
;;; Find the difference between the sum of the squares of the first one
;;; hundred natural numbers and the square of the sum.


This one's not so bad.

;;; Helper functions

(defun square (x)
  (expt x 2))

(defun sum-of-first (max)
  (sum (range 1 (+ max 1))))

(defun squared-sum (max)
  (squared (sum-of-first max)))

(defun squares (max)
  (mapcar (lambda (x) (square x)) (range 1 (+  max 1))))

(defun sum-of-squares (max)
  (sum (squares max)))

(defun sum-square-difference (max)
  (- (squared-sum max) (sum-of-squares max)))


;;; Solution

(print (sum-square-difference 100))
;; : 25164150
