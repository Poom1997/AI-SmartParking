
heuristic(Vertex, Ss):-
  create(Vertex, [Vertex], Ds),
  heuristic_1(Ds, [s(Vertex,0,[])], Ss).

heuristic_1([], Ss, Ss).
heuristic_1([D|Ds], Ss0, Ss):-
  best(Ds, D, S),
  delete([D|Ds], [S], Ds1),
  S=s(Vertex,Distance,Path),
  reverse([Vertex|Path], Path1),
  merge(Ss0, [s(Vertex,Distance,Path1)], Ss1),
  create(Vertex, [Vertex|Path], Ds2),
  delete(Ds2, Ss1, Ds3),
  incr(Ds3, Distance, Ds4),
  merge(Ds1, Ds4, Ds5),
  heuristic_1(Ds5, Ss1, Ss).

path(Vertex0, Vertex, Path, Dist):-
  heuristic(Vertex0, Ss),
  member(s(Vertex,Dist,Path), Ss), !.
  
create(Start, Path, Edges):-
  setof(s(Vertex,Edge,Path), e(Start,Vertex,Edge), Edges), !.
create(_, _, []).
  
best([], Best, Best).
best([Edge|Edges], Best0, Best):-
  shorter(Edge, Best0), !,
  best(Edges, Edge, Best).
best([_|Edges], Best0, Best):-
  best(Edges, Best0, Best).

shorter(s(_,X,_), s(_,Y,_)):-X < Y.

delete([], _, []). 
delete([X|Xs], [], [X|Xs]):-!. 
delete([X|Xs], [Y|Ys], Ds):-
  eq(X, Y), !, 
  delete(Xs, Ys, Ds). 
delete([X|Xs], [Y|Ys], [X|Ds]):-
  lt(X, Y), !, delete(Xs, [Y|Ys], Ds). 
delete([X|Xs], [_|Ys], Ds):-
  delete([X|Xs], Ys, Ds). 
  
merge([], Ys, Ys). 
merge([X|Xs], [], [X|Xs]):-!. 
merge([X|Xs], [Y|Ys], [X|Zs]):-
  eq(X, Y), shorter(X, Y), !, 
  merge(Xs, Ys, Zs).
merge([X|Xs], [Y|Ys], [Y|Zs]):-
  eq(X, Y), !, 
  merge(Xs, Ys, Zs).
merge([X|Xs], [Y|Ys], [X|Zs]):-
  lt(X, Y), !, 
  merge(Xs, [Y|Ys], Zs).
merge([X|Xs], [Y|Ys], [Y|Zs]):-
  merge([X|Xs], Ys, Zs).

eq(s(X,_,_), s(X,_,_)).  

lt(s(X,_,_), s(Y,_,_)):-X @< Y.

incr([], _, []).  
incr([s(V,D1,P)|Xs], Incr, [s(V,D2,P)|Ys]):-
  D2 is D1 + Incr,
  incr(Xs, Incr, Ys).

e(X, Y, Z):-node(X, Y, Z).
e(X, Y, Z):-node(Y, X, Z).
