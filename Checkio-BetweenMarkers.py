"""
You are given a string and two markers (the initial and final).
You have to find a substring enclosed between these two markers.
But there are a few important conditions:
-The initial and final markers are always different.
-If there is no initial marker then the beginning should be considered as the beginning of a string.
-If there is no final marker then the ending should be considered as the ending of a string.
-If the initial and final markers are mission then simply return the whole string.
-If the final marker is standing in front of the initial one then return an empty string.

Input: Three arguments. All of them are string. The second and third arguments are the initial and final markers.
Output: A string.
"""

begin = ">"
end = "<"
my_text = "What is >apple<"

#먼저 시작마커 들어있는 곳을 찾아서 그 자리 수를 알아내고 거기에 그 마커의 길이를 더하면 시작마커 다음 글자가 된다
#끝마커 들어있는 곳을 찾으면 거기까지 해서 자르면 되고 만약 끝마커 없으면 그 텍스트의 길이를 알아내서 맨마지막글자 뒤를 끝마커 위치로 지정한다
def between_markers (my_text, begin, end):
    #begin에 들어있는거부터 찾는데 이건 find함수로 찾기
    if begin in my_text:   #만약 begin에 해당하는 마커가 my_text안에 있으면, if가 돌아간다.
        begin_index = my_text.find(begin) + len(begin) #begin_index가 시작마커 그 다음 글자의 위치가 된다
    else:
        begin_index = 0 #만약 begin에 해당하는 마커가 없을때는 맨처음 글자에서부터 시작해야하므로 0가 된다
    
    if end in my_text: #만약 end에 해당하는 마커가 my_text안에 있으면 if가 작동한다
        end_index = my_text.find(end) #end의 경우에는 바로 하나 앞에까지만 찾으면 되니까 len구해서 더하는거 안한다
    else:
        end_index = len(my_text) #end마커에 해당하는 것이 my_text에 없으면 맨 끝까지 보내야 하므로 index를 my_text의 길이만큼으로 지정한다
    
    return my_text[begin_index:end_index] #마커 가운데 있는 애를 뽑아내기 위해서 슬라이싱한다

answer = between_markers(my_text, begin, end)

print(answer)
