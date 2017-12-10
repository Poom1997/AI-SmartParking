% explore all node (enqueue all connected node)
explore(S,Elt):- findall(N, node(S,N,_), Elt).
% use for 2nd case algorithm
explore(S,Elt,NewElt):- findall(N, node(S,N,_), Ep),
				append(Elt,Ep,NewElt).
%-----------------------------------------------------------------------------------------
%extract min of neigbor node (h(n) + g(n))  - consistent & admissible heuristic

exstract_min([H|T],Gn,Min) :-  exstract_min(T,H,Min,Gn).
exstract_min([],Min,Min,Gn):-!.
exstract_min([H|T],M,Min,Gn) :-  manhattan(H,X1), 
				 manhattan(M,Y2), 
				 (X1 + Gn)  =< (Y2+ Gn) ,  
				 exstract_min(T,H,Min,Gn).
exstract_min([H|T],M,Min,Gn) :-  manhattan(M,X1),
				 manhattan(H,Y2), 
				 (X1 + Gn) <  (Y2+ Gn),   
				 exstract_min(T,M,Min,Gn).
%-----------------------------------------------------------------------------------------
% go to next optimal node(Test)
nextNode(S,Gn,Min) :- explore(S,Elt), exstract_min(Elt,Gn,Min),!.

%-----------------------------------------------------------------------------------------
% Astar implementation
astar(S,G,Path) :- astar(S,G,0,[S],Path).
astar(G,G,_,Path,Path):- !.
astar(S,G,Gn,Path,Answer):- nextNode(S,Gn,Next),
				    Gn1 is Gn + 1,
				    append(Path,[Next],Path1),
				    astar(Next,G,Gn1,Path1,Answer).

%-----------------------------------------------------------------------------------------

%node 6 is destination
manhattan(n1,3).
manhattan(n2,2).
manhattan(n3,1).
manhattan(n4,4).
manhattan(n6,0).
manhattan(n7,3).
manhattan(n8,2).
manhattan(n9,1).