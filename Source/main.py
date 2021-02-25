import re
from pathlib import Path

"""
 Các hàm process_file(filename), parse_rulelist(rulelist, line),farse_and_unify(keys , values , i, name)
 xử lý file.
 
 xứ lý từ prolog sang list và dictionay: 
 như parent(A,B) --> 'parent(A,B)'
     parent(X,Y) :- parent(X,Z),parent(Z,Y)   -->  'parent(X,Y)' : ['parent(X,Z)','parent(Z,Y)']
     và goallist là các đích cần xét khi nhập từ console
     
 
 clauselist = ['parent(mary,bill)','parent(tom,bill','parent(tom,liz)']
 rulelist = {'parent(X,Y)' : ['parent(X,Z)','parent(Z,Y)']}
 goallist = ['parent(X,bill)']

 Tất nhiên các bài toán mình giải ko giải dc các bài toán đệ quy, mà là cơ bản.

"""

#////////////////////////////////////////////////////////////////////////////////////////////////////////////


def farse_and_unify(keys , values , i, name):
    new_name = name + str(i)
    keys = keys.replace(name,new_name)
    
    for i in range(len(values)):
        values[i] = values[i].replace(name,new_name)
    
    return dict([(keys,values)])
    
    
def parse_rulelist(rulelist, line):
    if '+' not in line:
        parse_rule = line.split(':-')
        rulelist.update(dict([(parse_rule[0].strip(),re.findall(r'\w+\([\w,]+\)', parse_rule[1]))]))
    else:
        parse_rule = line.split(':-')

        name = re.findall(r'\w+', parse_rule[0])[1]
        rule = parse_rule[1].split('),')
        rule = [s + ')' for s in rule]


        contains_plus = []
        contains_no_plus = []
        unify = []

        for i in rule:
            if '+' in i:
                contains_plus.extend(re.findall(r'\w+\([\w,]+\)', i))
            else:
                contains_no_plus.extend(re.findall(r'\w+\([\w,]+\)', i))

        for i in contains_plus:
            contains_no_plus.append(i)
            unify.append(contains_no_plus.copy())
            contains_no_plus.remove(i)


        for i in range(len(unify)):
            new_rule = farse_and_unify(parse_rule[0],unify[i], i, name)
            rulelist.update(new_rule)
            
        
def process_file(filename):
    flag = []
    file = open(filename)
    for line in file:
        if line[0].isalpha():
            line = line.replace(" ", "")
            flag.append(line[:-2])
    file.close()
            
    rulelist ={}
    clauselist=[]
    
    for line in flag:
        if ':-' in line:
            parse_rulelist(rulelist, line)
        else:
            clauselist.extend(re.findall(r'\w+\([\w,]+\)', line))
        
    _clauselist = []
    [_clauselist.append(x) for x in clauselist if x not in _clauselist] 

    return _clauselist, rulelist
    

    
    
    
#//////////////////////////////////////////////////////////////////////////////////////////////////////////////    
    
#clauselist, rulelist = process_file("hello.pl")          






 
#/////////////////////////////////////////////////////////////////////////////////////////////////////

def change_goal_in_rulelist(goal,rule,goallist):
    
    ds = ['A','B','C','D','E','F','G','H','J']
    dup_arguments = []
    for goall in goallist:
        dup_arguments.extend(re.findall(r'\([\w,]+\)', goall)[0].strip('()').split(','))
        
    #danh sach cac bien ton tai trong goallist
    arguments_goallist = []
    [arguments_goallist.append(x) for x in dup_arguments if x not in arguments_goallist] 
    
    

    arguments_of_goal = re.findall(r'\([\w,]+\)', goal)[0].strip('()').split(',')
    arguments_of_rule = re.findall(r'\([\w,]+\)', rule)[0].strip('()').split(',') #XZ
    
    
    

    temp_rule = rulelist[rule].copy()

    for _rule in temp_rule:
        list_arg = re.findall(r'\([\w,]+\)', _rule)[0].strip('()').split(',') #xy
        temp_list_arg = list_arg.copy()
        

        for element in list_arg: #y
            if element not in arguments_of_rule :# and phantu not in bentrong_goal:
                for i in ds:
                    if i not in arguments_goallist:
                        list_arg[list_arg.index(element)] = i
                        break
                        
        kpop = ",".join(list_arg)
        vpop = ",".join(temp_list_arg)
        
        temp_rule[temp_rule.index(_rule)] = _rule.replace(vpop, kpop)

        
    for _rule in temp_rule:
        list_arg = re.findall(r'\([\w,]+\)', _rule)[0].strip('()').split(',')
        temp_list_arg = list_arg.copy()
        
        for element in list_arg:
            if element in arguments_of_rule:
                list_arg[list_arg.index(element)] = arguments_of_goal[arguments_of_rule.index(element)]
        
        
        
        kpop = ",".join(list_arg)
        vpop = ",".join(temp_list_arg)
        
        temp_rule[temp_rule.index(_rule)] = _rule.replace(vpop, kpop)
    
    return temp_rule

    
    
    
    
def goal_not_in_rulelist(goallist):  #goal_not_in_rulelist
    for goal in goallist:
        for rule in rulelist:
            if re.findall(r'\w+\(',goal) == re.findall(r'\w+\(',rule):
                return False
    return True
 

        
        
def match_rulelist(goallist,test_list):
    in_rulelist = False   
    for goal in goallist:
        for rule in rulelist:
            if re.findall(r'\w+\(',goal) == re.findall(r'\w+\(',rule):  #nếu goal nằm trong rulelist,(phân tích nhỏ goal từ rule )
                new_goallist = goallist.copy()                          #vì đệ quy nên phải sao chép, từ nhiều rule
                new_goallist.remove(goal)
                new_goallist.extend(change_goal_in_rulelist(goal ,rule, goallist))  

                match_rulelist(new_goallist,test_list)        #đệ quy sau mỗi lần tìm dc rule
                in_rulelist = True
                      
        if in_rulelist == True:                     #vì đề quy nên return, tránh phân tích trùng lặp
            return
            
        if goal_not_in_rulelist(goallist) == True:  #vì ko thể phân tích nhỏ ra các rule thì dừng, chi xet trong rulelist
            test_list.append(goallist)
            return
        

        
#///////////////////////////////////////////////////////////////////////////////////////////////        
        
def all_arguments_in_clauselist(clauselist): #cacbienbentrongclause
    dup_arguments = []
    for clause in clauselist:
        dup_arguments.extend(re.findall(r'\([\w,]+\)', clause)[0].strip('()').split(','))

    arguments = []
    [arguments.append(x) for x in dup_arguments if x not in arguments] 
    return arguments

#arguments_clauselist = all_arguments_in_clauselist(clauselist)

def goal_contains_variables(goal): #goalcothethaythe
    
    arguments_of_goal = re.findall(r'\([\w,]+\)', goal)[0].strip('()').split(',')
    
    if 'answer' in goal:
        return False
    
    for argument in arguments_of_goal:
        if argument not in arguments_clauselist and argument[0].isupper() == True:
            return True
        
    return False

def rule_and_goal_are_homogenous(goal, clause): #ruletuongdongvoigoal
    
    if re.findall(r'\w+\(',goal) != re.findall(r'\w+\(',clause):
        return False
    
    arguments_of_clause = re.findall(r'\([\w,]+\)', clause)[0].strip('()').split(',')
    arguments_of_goal = re.findall(r'\([\w,]+\)', goal)[0].strip('()').split(',')
    
    if len(arguments_of_clause) != len(arguments_of_goal):
        return False
    
    replacements = dict(zip(arguments_of_goal, arguments_of_clause))
    
    for i in replacements:
        if i in arguments_clauselist and i != replacements[i]:
            return False
        
    return replacements

def unify(new_goallist,replacements):  #replace_variables_in_goallist

    for goal in new_goallist:
        arguments_of_goal = re.findall(r'\([\w,]+\)', goal)[0].strip('()').split(',')
        temp_arguments_of_goal = arguments_of_goal.copy()
        
        for argument in arguments_of_goal:
            if argument in replacements:
                arguments_of_goal[arguments_of_goal.index(argument)] = replacements[argument]
        
        
        vpop = ",".join(arguments_of_goal)
        kpop = ",".join(temp_arguments_of_goal)
        
        new_goallist[new_goallist.index(goal)] = goal.replace(kpop, vpop)
  

def exist_in_clauselist(new_goallist): #kiemtraneutontaicaisai
    for goal in new_goallist:
        if 'answer' not in goal and goal_contains_variables(goal) == False:
            if goal not in clauselist:
                return False
    return True





def match_clauselist(goallist,result):
    for goal in goallist:
        if goal_contains_variables(goal) == True:    #nếu goal chứa các biến vd: hello(X,Y), kiểm tra và thay thế vs các clause fit
            for clause in clauselist:
                replacements = rule_and_goal_are_homogenous(goal,clause) #nếu tìm được thì cho replacements dict tương ứng, để đồng nhất
                if replacements != False:                                
                    new_goallist = goallist.copy()                       #thay the để đệ quy, vì còn nhiều clause để xét
                    unify(new_goallist, replacements)                    # đồng nhất biến
                    if exist_in_clauselist(new_goallist) == False:       #sau khi đồng nhất nếu tồn tại 1 goal ko tồn tại trong clauselist
                        continue
                    match_clauselist(new_goallist,result)   #đề quy tìm tiếp, mỗi clause tìm dc đều đệ quy
            return                                   #vì goal sau khi đệ quy, sẽ xét đệ quy sau, nên return để tránh trùng lặp      
        else:
            if 'answer' not in goal and goal not in clauselist:
                return
    result.append(goallist)
    
    

#/////////////////////////////////////////////////////////////////////////////////////////   


def output_answer(goallist):
    for goal in goallist:
        if 'answer' in goal:
            return re.findall(r'\([\w,]+\)', goal)[0].strip('()')


def solve(goallst,  name ):   #mot tap cau hoi
    
    cotraloi = True
    if len(name) == 0:
        cotraloi = False
    
    all_results = []
    
    test_list = []
    match_rulelist(goallst, test_list)
    
    for goal_case in test_list:
        result = []
        match_clauselist(goal_case,result)
        all_results.extend(result)
 

    if (cotraloi == False):
        if len(all_results) == 0:
            print ("false")
        else:
            print ("true")
    else:
        if len(all_results) == 0:
            print ("false")
        else:
            for rel in all_results:
                answer = output_answer(rel)
                strig = name + " = "+ answer + " "
                goon = input(strig)
                if goon != ';':
                    break
                


def check_input(_goallistt): #chi xu ly co (), va qua doi so va ten bien
    name = ""
    if '(' not in _goallistt or ')' not in _goallistt:
        return False, name, []
    
    arr_goallist = []
    arr_goallist.extend(re.findall(r'\w+\([\w,]+\)', _goallistt))
    
    
    temp_goallist = []
    temp_goallist.extend(re.findall(r'\([\w,]+\)', _goallistt))
    
    
    ds = []
    for i in temp_goallist:
        ds.extend(i.strip('()').split(','))
        
    check = 0;
    for i in ds:
        if i not in arguments_clauselist:
            name = i
            check += 1
    
    if check > 1:
        return False,name, []
    
    
    
    if name[0].isupper() == False:
        name = ""

    
    if name != "":
        _add = 'answer({0})'.format(name)
        arr_goallist.append(_add)
        
    return True,name,arr_goallist





def main():
    _goallist = ""

    global arguments_clauselist 
    global rulelist 
    global goallist
    global clauselist 
    
    file_name = input("Enter file: ")
    my_file = Path(file_name)
    if my_file.is_file() == False:
        print("The file does not exist!")
        return

    while True:

        clauselist, rulelist = process_file(file_name)  
        arguments_clauselist = all_arguments_in_clauselist(clauselist)
        
        _goallist = input("?- " )
        if _goallist in ['exit','exit.','.']:
            return
        if _goallist in ['true', 'false']:
            print(_goallist)
            continue
            
        is_next, name,_arrgoallist = check_input(_goallist)   #chi xu ly co (), va qua doi so va ten bien

        if is_next == False:
            print('false - over arguments')
        else:
            solve(_arrgoallist,name)
            
        
main()
