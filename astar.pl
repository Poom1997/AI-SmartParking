% explore all node (enqueue all connected node)
explore(S,Elt):- findall(N, node(S,N,_), Elt).
% use for 2nd case algorithm
explore(S,Elt,NewElt):- findall(N, node(S,N,_), Ep),
				append(Elt,Ep,NewElt).

%extract min of neigbor node (h(n) + g(n))  - consistent & admissible heuristic
%n999 use to mark at Greatest number
manhattan(n999,999).
exstract_min(Elt,Inc, Min) :- findmin(Elt,Inc,n999,Min).
findmin([],_,_,Min).
findmin([H|T],Inc,Temp,Min) :- manhattan(H,X) ,write('pass1'),
					 manhattan(Temp,Y) ,write(Y + Inc),
					 (Y + Inc) >= (X + Inc) ,
					 findmin(T,Inc,H,H),!.
findmin([H|T],Inc,Temp,Min) :- manhattan(H,X) ,
					 manhattan(Temp,Y) ,
					 (Y + Inc) =< (X + Inc) ,
					 findmin(T,Inc,Temp,Min).

% append optimal node to path_list

% dequeue = extract-min node (least f(n) = g(n) + h(n))
dequeue([H|T], H ,T).

%Test access index
test(S,Result) :- explore(S,Elt), match(Elt,0,Result).

%loop to access item
match([H|_],0,H) :- !.
match([_|T],N,H) :-N > 0, 
    			 N1 is N-1,
    			 match(T,N1,H).