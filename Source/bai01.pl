/**male*/
male(pPhillip).
male(pCharles).
male(cmPhillips).
male(tLaurence).
male(pAndrew).
male(pEdward).
male(pWilliam).
male(pHarry).
male(peterPhillips).
male(mTindall).
male(jvSevern).
male(pGeorge).
male(mgTindall).
/**female*/
female(qElizabethII).
female(pDiana).
female(cpBowles).
female(pAnne).
female(sFerguson).
female(srJones).
female(kMiddleton).
female(aKelly).
female(zPhillips).
female(pBeatrice).
female(pEugenie).
female(llmWindsor).
female(pCharlotte).
female(sPhillips).
female(iPhillips).

/**parent*/

/**The he 1*/
parent(qElizabethII,pCharles).
parent(pPhillip,pCharles).
parent(qElizabethII,pAnne).
parent(pPhillip,pAnne).
parent(qElizabethII,pAndrew).
parent(pPhillip,pAndrew).
parent(qElizabethII,pEdward).
parent(pPhillip,pEdward).
/**The he 2*/
parent(pDiana,pWilliam).
parent(pCharles,pWilliam).
parent(pDiana,pHarry).
parent(pCharles,pHarry).

parent(cmPhillips,peterPhillips).
parent(pAnne,peterPhillips).
parent(cmPhillips,zPhillips).
parent(pAnne,zPhillips).

parent(sFerguson,pBeatrice).
parent(pAndrew,pBeatrice).
parent(sFerguson,pEugenie).
parent(pAndrew,pEugenie).

parent(srJones,jvSevern).
parent(pEdward,jvSevern).
parent(srJones,llmWindsor).
parent(pEdward,llmWindsor).

/**The he 3*/
parent(pWilliam,pGeorge).
parent(kMiddleton,pGeorge).
parent(pWilliam,pCharlotte).
parent(kMiddleton,pCharlotte).

parent(aKelly,sPhillips).
parent(peterPhillips,sPhillips).
parent(aKelly,iPhillips).
parent(peterPhillips,iPhillips).

parent(zPhillips,mgTindall).
parent(mTindall,mgTindall).

/**married*/

married(qElizabethII,pPhillips).
married(pPhillips,qElizabethII).

married(pCharles,cpBowles).
married(cpBowles,pCharles).

married(pAnne,tLaurence).
married(tLaurence,pAnne).

married(srJones,pEdward).
married(pEdward,srJones).

married(pWilliam,kMiddleton).
married(kMiddleton,pWilliam).

married(aKelly,peterPhillips).
married(peterPhillips,aKelly).

married(zPhillips,mTindall).
married(mTindall,zPhillips).

/**divorced*/
divorced(pDiana,pCharles).
divorced(pCharles,pDiana).

divorced(cmPhillips,pAnne).
divorced(pAnne,cmPhillips).

divorced(sFerguson,pAndrew).
divorced(pAndrew,sFerguson).

/**Kiem tra dung sai*/
husband(Person,Wife):-married(Person,Wife),male(Person).
wife(Person,Husband):-married(Person,Husband),female(Person).
father(Parent,Child):-parent(Parent,Child),male(Parent).
mother(Parent,Child):-parent(Parent,Child),female(Parent).
child(Child,Parent):-parent(Parent,Child).
son(Child,Parent):-parent(Parent,Child),male(Child).
daughter(Child,Parent):-parent(Parent,Child),female(Child).

/**Kiem tra chau*/
grandparent(GP,GC):-parent(X,GC),parent(GP,X).
grandmother(GM,GC):-mother(X,GC),mother(GM,X).
grandfather(GF,GC):-father(X,GC),father(GF,X).
grandchild(GC,GP):-grandparent(GP,GC).
grandson(GS,GP):-grandchild(GS,GP),male(GS).
granddaughter(GD,GP):-grandchild(GD,GP),female(GD).

sibling(Person1,Person2):-father(X,Person1),child(Person2,X).
brother(Person,Sibling):-sibling(Person,Sibling),male(Person).
sister(Person,Sibling):-sibling(Person,Sibling),female(Person).
aunt(Person,NieceNephew):-parent(X,NieceNephew),sibling(X,Person),female(Person).
uncle(Person,NieceNephew):-parent(X,NieceNephew),sibling(X,Person),male(Person).
niece(Person,AuntUncle):-(aunt(AuntUncle,Person)+uncle(AuntUncle,Person)),female(Person).
nephew(Person,AuntUncle):-(aunt(AuntUncle,Person)+uncle(AuntUncle,Person)),male(Person).