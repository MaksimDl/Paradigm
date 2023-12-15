sum([], 0).
sum([H|T], S) :-
   sum(T, ST),
   S is ST + H.

?- sum([1,2,3,4,5,6,7,8,9,10], X).
X = 15.