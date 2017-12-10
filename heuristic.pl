% heuristic(Vertex0, Ss) is true if Ss is a list of structures s(Vertex, Dist,
%   Path) containing the shortest Path from Vertex0 to Vertex, the distance of
%   the path being Dist.  The graph is defined by e/3.
% e.g. heuristic(penzance, Ss)
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

% path(Vertex0, Vertex, Path, Dist) is true if Path is the shortest path from
%   Vertex0 to Vertex, and the length of the path is Dist. The graph is defined
%   by e/3.
% e.g. path(penzance, london, Path, Dist)
path(Vertex0, Vertex, Path, Dist):-
  heuristic(Vertex0, Ss),
  member(s(Vertex,Dist,Path), Ss), !.
  
% create(Start, Path, Edges) is true if Edges is a list of structures s(Vertex,
%   Distance, Path) containing, for each Vertex accessible from Start, the
%   Distance from the Vertex and the specified Path.  The list is sorted by the
%   name of the Vertex.
create(Start, Path, Edges):-
  setof(s(Vertex,Edge,Path), e(Start,Vertex,Edge), Edges), !.
create(_, _, []).
  
% best(Edges, Edge0, Edge) is true if Edge is the element of Edges, a list of
%   structures s(Vertex, Distance, Path), having the smallest Distance.  Edge0
%   constitutes an upper bound.
best([], Best, Best).
best([Edge|Edges], Best0, Best):-
  shorter(Edge, Best0), !,
  best(Edges, Edge, Best).
best([_|Edges], Best0, Best):-
  best(Edges, Best0, Best).

shorter(s(_,X,_), s(_,Y,_)):-X < Y.

% delete(Xs, Ys, Zs) is true if Xs, Ys and Zs are lists of structures s(Vertex,
%   Distance, Path) ordered by Vertex, and Zs is the result of deleting from Xs
%   those elements having the same Vertex as elements in Ys.
delete([], _, []). 
delete([X|Xs], [], [X|Xs]):-!. 
delete([X|Xs], [Y|Ys], Ds):-
  eq(X, Y), !, 
  delete(Xs, Ys, Ds). 
delete([X|Xs], [Y|Ys], [X|Ds]):-
  lt(X, Y), !, delete(Xs, [Y|Ys], Ds). 
delete([X|Xs], [_|Ys], Ds):-
  delete([X|Xs], Ys, Ds). 
  
% merge(Xs, Ys, Zs) is true if Zs is the result of merging Xs and Ys, where Xs,
%   Ys and Zs are lists of structures s(Vertex, Distance, Path), and are
%   ordered by Vertex.  If an element in Xs has the same Vertex as an element
%   in Ys, the element with the shorter Distance will be in Zs.
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

% incr(Xs, Incr, Ys) is true if Xs and Ys are lists of structures s(Vertex,
%   Distance, Path), the only difference being that the value of Distance in Ys
%   is Incr more than that in Xs.
incr([], _, []).  
incr([s(V,D1,P)|Xs], Incr, [s(V,D2,P)|Ys]):-
  D2 is D1 + Incr,
  incr(Xs, Incr, Ys).

% member(X, Ys) is true if the element X is contained in the list Ys.
%member(X, [X|_]).
%member(X, [_|Ys]):-member(X, Ys).

% reverse(Xs, Ys) is true if Ys is the result of reversing the order of the
%   elements in the list Xs.
%reverse(Xs, Ys):-reverse_1(Xs, [], Ys).

%reverse_1([], As, As).
%reverse_1([X|Xs], As, Ys):-reverse_1(Xs, [X|As], Ys).

e(X, Y, Z):-node(X, Y, Z).
e(X, Y, Z):-node(Y, X, Z).
