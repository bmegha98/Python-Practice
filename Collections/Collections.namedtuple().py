from collections import namedtuple
if __name__=='__main__':
    N=int(input())
    avg=0
    sheet=input().split()
    #print(sheet)
    student=namedtuple('student',[sheet[0],sheet[1],sheet[2],sheet[3]])
    for i in range(N):
        stu=input().split()
        S=student(stu[0],stu[1],stu[2],stu[3])
        avg+=int(S.MARKS)
    print("{:.2f}".format(avg/N))
