;;;; Project Euler: an exercise in inductive chain learning
;;;; Problem 4: Largest palindrome product

;;; A palindromic number reads the same both ways. The largest palindrome made
;;; from the product of two 2-digit numbers is \( 9009 = 91*99 \).
;;;
;;; Find the largest palindrome made from the product of two 3-digit numbers.


;;; Helper functions

(defun is-palindrome (num)
  ;; Checks if a string is palindromic.
  (let ((num-string (write-to-string num)))
       (equalp (reverse num-string) num-string)))


;;; Tests

(print (is-palindrome "PANAMA"))
;; : NIL
(print (is-palindrome "AMANAPLANACANALPANAMA"))
;; : T


;;; Solution

;; The function *largest-palindrome* iterates from a given number /max/ down
;; to 1. For each iteration, it iterates a second time from /max/ to 1. If the
;; product is a palindrome greater than the variable /palindrome/, it
;; overwrites it, ultimately returning its final value:

 (defun largest-palindrome (max)
   (setq palindrome 0)
   (loop named outer for i downfrom max to 1 do
     (loop for j downfrom max to 1 do
       (when (and
              (is-palindrome (* i j))
              (> (* i j) palindrome))
             (setq palindrome (* i j)))))
   palindrome)

(print (largest-palindrome 999))
;; : 906609



