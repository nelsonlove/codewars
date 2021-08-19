;;;; Project Euler: an exercise in inductive chain learning
;;;; Problem 7: 10001st prime

;;; By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
;;; that the 6th prime is 13.
;;;
;;; What is the 10,001st prime number?


;;; Helper functions

(defun is-prime (n)
  (if (< n 2)
      nil
      (every 'null (loop for x from 2 to (+ 1 (isqrt n)) collect
        (equal (mod n x) 0)))))

(defun nth-prime (n)
  (defun prime-acc (l n p)
    (if (equal (length l) n)
        (last l)
        (if (is-prime p)
            (prime-acc (append l (list p)) n (+ p 1))
            (prime-acc l n (+ p 1)))))
  (prime-acc '(2) n 2))


;;; Solution

(print (nth-prime 10001))
;; : 104743
