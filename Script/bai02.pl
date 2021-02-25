
%  information of  employee.
manage(nguyenphuocquang).

% a list of type book

type(self_development_book).
type(history_book).
type(geography_book).
type(science_book).

% author
author(nguyenvanA).
author(nguyenvanB).
author(nguyenvanC).
author(nguyenvanD).
author(nguyenvanF).
author(nguyenvanG).
author(nguyenvanH).
author(nguyenvanL).



% manage author in a type of  book.


manage_author(self_development_book,nguyenvanA).
manage_author(self_development_book,nguyenvanB).

manage_author(history_book,nguyenvanC).
manage_author(history_book,nguyenvanD).
manage_author(history_book,nguyenvanA).

manage_author(geography_book,nguyenvanF).
manage_author(geography_book,nguyenvanG).

manage_author(science_book,nguyenvanH).
manage_author(science_book,nguyenvanL).
% mange book

manage_book(self_development_book,book_sdb_a).
manage_book(self_development_book,book_sdb_b).
manage_book(self_development_book,book_sdb_c).
manage_book(self_development_book,book_sdb_d).


manage_book(history_book,book_hb_a).
manage_book(history_book,book_hb_b).
manage_book(history_book,book_hb_c).


manage_book(geography_book,book_gb_a).
manage_book(geography_book,book_gb_b).
manage_book(geography_book,book_gb_c).



manage_book(science_book,book_sb_a).
manage_book(science_book,book_sb_b).
manage_book(science_book,book_sb_c).





book(nguyenvanA,book_sdb_a).
book(nguyenvanA,book_sdb_c).
book(nguyenvanA,book_sdb_b).

book(nguyenvanB,book_sdb_d).


book(nguyenvanA,book_hb_a).
book(nguyenvanC,book_hb_b).
book(nguyenvanD,book_hb_c).

book(nguyenvanG,book_gb_a).
book(nguyenvanF,book_gb_b).
book(nguyenvanF,book_gb_c).

book(nguyenvanH,book_sb_a).
book(nguyenvanH,book_sb_b).
book(nguyenvanL,book_sb_c).

% number of each book.

number_book(book_sdb_a,10).
number_book(book_sdb_b,10).
number_book(book_sdb_c,10).
number_book(book_sdb_d,10).


number_book(book_hb_a,10).
number_book(book_hb_b,10).
number_book(book_hb_c,10).


number_book(book_gb_a,10).
number_book(book_gb_c,10).
number_book(book_gb_b,10).


number_book(book_sb_a,10).
number_book(book_sb_b,10).
number_book(book_sb_c,10).

% information of borrower
borrower(lethiA).
borrower(lethiB).
borrower(lethiC).
borrower(lethiD).
borrower(lethiF).
borrower(lethiK).
borrower(lethiQ).
borrower(lethiM).

borrower_book(lethiA,book_sdb_a).
borrower_book(lethiB,book_sdb_b).
borrower_book(lethiC,book_hb_b).
borrower_book(lethiD,book_hb_b).
borrower_book(lethiA,book_gb_b).
borrower_book(lethiK,book_gb_a).
borrower_book(lethiQ,book_sc_a).
borrower_book(lethiM,book_sc_a).
borrower_book(lethiB,book_sc_b).



%location

location(location_a).
location(location_b).
location(location_c).
location(location_d).

% manage book
location_book(location_a,book_sdb_a).
location_book(location_a,book_sdb_b).
location_book(location_a,book_sdb_c).
location_book(location_a,book_sdb_d).


location_book(location_b,book_hb_a).
location_book(location_b,book_hb_b).
location_book(location_b,book_hb_c).


location_book(location_c,book_gb_a).
location_book(location_c,book_gb_a).
location_book(location_c,book_gb_a).



location_book(location_d,book_sb_a).
location_book(location_d,book_sb_a).
location_book(location_d,book_sb_a).




%  X: type of book ,Z:author to find all book of author in one type
find_author(X,Z):-manage_author(X,Y),book(Y,Z).
%  X: author write about two field
checking(X,Z,R):-manage_author(Z,X),manage_author(R,X),Z\==R.

%  X: type of book.
%  Y:title of book.
%  N : number of book.
numberbook(X,Y,N):- manage_book(X,Y),number_book(Y,N).

% X : name of  borrower.
% Y:  type of book.

lovefield(X,Y):-borrower_book(X,Z),manage_book(Y,Z).



% The book about field.
% X: Title of book
% Y:  Type of book
find_field(X,Y):- manage_book(Y,X).



% find  location of author.
% X: author.
% Y: location.
find_location(X,Y):-location_book(Y,Z),book(X,Z).








