;;;; Project Euler: an exercise in inductive chain learning
;;;; Problem 5: Smallest multiple

;;; 2520 is the smallest number that can be divided by each of the numbers
;;; from 1 to 10 without any remainder.
;;;
;;; What is the smallest positive number that is evenly divisible by all
;;; of the numbers from 1 to 20?


;;; Helper functions

 (defun evenly-divisible (num l)
   ;; Takes a list of integers /l/ and checks if an integer /num/ is evenly
   ;; divisible by all of them, returning /num/ if so.
   (when (every #'(lambda (x) (is-factor-of num x)) l) num))


;;; Tests


;; (print (evenly-divisible 18 (range 1 4)))
;; : 18
;; (print (evenly-divisible 18 (range 1 5)))
;; : NIL


;;; Solution

(defun smallest-evenly-divisible (max)
  ;; Takes an integer /max/ and returns the smallest positive number evenly
  ;; divisible by all natural numbers from 1 to /max/.
  (loop for i from 1
   thereis (evenly-divisible i (range 1 (+ max 1)))))


;; This is accurate but the function is very slow:

(print (smallest-evenly-divisible 20))
;; : 232792560

;; How to optimize? It's checking each iteration of i for every natural number
;; from 1 to 20. But we can decompose the composite numbers...

;; Here's the prime factor function from the earlier problem:

(defun factorize (num)
  (defun prime-acc (dividend divisor divisors)
    (let ((quotient (/ dividend divisor)))
         (cond
           ((equal quotient 1) (append (list divisor) divisors))
           ((integerp quotient)
              (prime-acc quotient divisor (append (list divisor) divisors)))
           (T (prime-acc dividend (+ 1 divisor) divisors)))))
  (prime-acc num 2 nil))

;; Next, another helper function:

 (defun list-difference (list1 list2)
   ;; Returns the difference between two lists.
   (let ((output list2))
     (mapc (lambda (x)
         (setq output (remove x output :count 1)))
       list1)
     output))
 #+END_SRC

;; Then the main function:

(defun smallest-evenly-divisible-fast (max)
  (setq factors nil)
  (loop for i from max downto 2 do
    (setq factors (append factors (list-difference factors (factorize i)))))
  (apply '* factors))

;; And our test:

(print (smallest-evenly-divisible-fast 20))
;; : 232792560

;; So much faster!