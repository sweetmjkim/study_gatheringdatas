import bulls_subfunction_js as subfunction_js
import bulls_subfunction_mj as subfunction_mj
# 기본 function 형식 - 기다림. 불리울 때 기능한다. def function () : -> tap pass -> return 0
def main() :
    try:   # 업무 코드
        pass
    except :
        pass    # 업무 코드 문제 발생 시 대처 코드
    finally :
        pass
    return 0

if __name__ == "__main__":
    try:
        main()    # 업무 코드
    except:
        pass    # 업무 코드 문제 발생 시 대처 코드
    finally :
        pass    # try나 except이 끝난 후 무조건 실행 코드