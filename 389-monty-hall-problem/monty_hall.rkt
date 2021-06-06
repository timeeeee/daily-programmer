#lang racket

; Monty hall problem
; https://www.reddit.com/r/dailyprogrammer/comments/n94io8/20210510_challenge_389_easy_the_monty_hall_problem/

(require racket/random)

; return true if the player one the prize
; start-strategy returns a number, 1-3
; switch-strategy takes the originally chosen door, and the revealed door, and returns a new choice 1-3
(define play-monty-hall
  (λ (start-strategy switch-strategy)
    ; pick a free door to reveal
    (define revealed-door
      (λ (prize-door first-door)
        (let ([available (filter (λ (x) (not (or (= x prize-door) (= x first-door)))) '(1 2 3))])
          (random-ref available))))
    (let (
          [prize-door (+ (random 3) 1)]
          [first-door (start-strategy)])
      (= prize-door
         (switch-strategy first-door (revealed-door prize-door first-door))))))

; Run a number of simulations with the given strategy and return fraction of wins
(define simulate
  (λ (num-simulations first-strategy switch-strategy)
    (define boolean->int (λ (x) (if x 1 0)))
    ; (define sum (λ (seq) (foldl + 0 seq)))
    (define mean (λ (seq) (/ (foldl + 0.0 seq) (length seq))))
    (mean (build-list
          num-simulations
          (λ (x) (boolean->int (play-monty-hall first-strategy switch-strategy)))))))


; strategies
; ==========

(define make-pick-n-strategy  ; make a strategy that always returns the given door
  (λ (n)
    (λ _ n)))

(define pick-1-strategy (make-pick-n-strategy 1))
(define pick-2-strategy (make-pick-n-strategy 2))
(define pick-3-strategy (make-pick-n-strategy 3))

(define switch-strategy
  (λ (first-door revealed-door) (- (+ 1 2 3) first-door revealed-door)))

(define keep-strategy
  (λ (first-door revealed-door) first-door))

(define pick-random-door-strategy (λ () (+ (random 3) 1)))

; randomly select between keeping and switching
(define random-switch-strategy
  (λ (first-door revealed-door)
    ((if (< (random) .5) keep-strategy switch-strategy) first-door revealed-door)))


; output
; ======

(display "alice always chooses door 1 and keeps it\n")
(display "win rate in 1000 games: ")
(display (simulate 1000 pick-1-strategy keep-strategy))
(newline)

(display "bob always chooses door 1 and then switches\n")
(display "win rate in 1000 games: ")
(display (simulate 1000 pick-1-strategy switch-strategy))
(newline)

(display "carol chooses random from available options in both steps\n")
(display "win rate in 1000 games: ")
(display (simulate 1000 pick-random-door-strategy random-switch-strategy))
(newline)

(display "dave chooses randomly at first and then sticks with his door\n")
(display "win rate in 1000 games: ")
(display (simulate 1000 pick-random-door-strategy keep-strategy))
(newline)

(display "erin chooses randomly at first and always switches doors\n")
(display "win rate in 1000 games: ")
(display (simulate 1000 pick-random-door-strategy switch-strategy))
(newline)

(display "frank choose door 1 at first and then switches to door 2 *if* it's available\n")
(display "win rate in 1000 games: ")
(display (simulate 1000 pick-1-strategy
                   (λ (first-door revealed-door)
                     (if (= revealed-door 2) 1 2))))
(newline)

(display "gina starts with alices strategy, and switches alice/bob any time she loses\n")
(display ":(")




; tests!
; ======

(require rackunit)

(check-equal? (pick-1-strategy) 1)
(check-equal? (pick-1-strategy 0 0) 1)
(check-equal? (pick-2-strategy) 2)
(check-equal? (pick-2-strategy 0 0) 2)
(check-equal? (pick-3-strategy) 3)
(check-equal? (pick-3-strategy 0 0) 3)

(check-equal? (keep-strategy 1 2) 1)
(check-equal? (keep-strategy 1 3) 1)
(check-equal? (keep-strategy 2 1) 2)
(check-equal? (keep-strategy 2 3) 2)
(check-equal? (keep-strategy 3 1) 3)
(check-equal? (keep-strategy 3 2) 3)

(check-equal? (switch-strategy 1 2) 3)
(check-equal? (switch-strategy 1 3) 2)
(check-equal? (switch-strategy 2 1) 3)
(check-equal? (switch-strategy 2 3) 1)
(check-equal? (switch-strategy 3 1) 2)
(check-equal? (switch-strategy 3 2) 1)

