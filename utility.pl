% Park node for optimal

parknode(PList,Result) :- parkmin(PList,999,n0,Result).
parkmin([],_,Result,Result) :- !.
parkmin([H|T],Min,Minnode,Result) :-  findall(Y,park(H,Y),TList),
					sort(TList,[H1|T1]),
					H1 =< Min,
					parkmin(T,H1,H,Result).

parkmin([H|T],Min,Minnode,Result) :-  findall(Y,park(H,Y),TList),
					sort(TList,[H1|T1]),
					H1 > Min,
					parkmin(T,Min,Minnode,Result).


% Exit node for optimal
exitnode(PList,Result) :- exitmin(PList,999,n0,Result).
exitmin([],_,Result,Result) :- !.
exitmin([H|T],Min,Minnode,Result) :-  findall(Y,exit(H,Y),TList),
					sort(TList,[H1|T1]),
					H1 =< Min,
					exitmin(T,H1,H,Result).

exitmin([H|T],Min,Minnode,Result) :-  findall(Y,exit(H,Y),TList),
					sort(TList,[H1|T1]),
					H1 > Min,
					exitmin(T,Min,Minnode,Result).




