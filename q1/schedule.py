"""
Loraine and Charles have a nearly 3-year-old child! Although their child is more independent
now, scheduling activities and household tasks remains challenging for them.
They have a list of N daily activities. Each activity occurswithin a specified time interval. They must
assign each activity to one of them, ensuring that neither person is responsible for two overlapping
activities. An activity ending at time t does not overlap with another starting at time t.
For example, suppose Loraine and Charles need to cover three activities: one from 18:00 to 20:00,
another from 19:00 to 21:00, and another from 22:00 to 23:00. One option is for Charles to handle
the activity from 19:00 to 21:00 while Loraine covers the other two. Another valid schedule could
have Loraine covering the activity from 18:00 to 20:00, with Charles covering the other
two. Note that the first two activities overlap between 19:00 and 20:00, so they cannot be assigned
to the same person.
Given the start and end times of each activity, find any schedule where the same person doesn't
handle overlapping activities, or state that it is impossible.

Input
The first line of input specifies the number of test cases, T.
Each test case begins with a line containing a single integer N, indicating the number of activities to
be assigned.
Then, N lines follow. The i-th line (starting from 1) contains two integers Si and Ei.
The i-th activity starts exactly Si minutes after midnight and ends exactly Ei minutes after midnight.

Output
For each test case, output one line containing Case #x: y, where x is the test case number (starting
from 1) and y is IMPOSSIBLE if there is no valid schedule according to the above rules, or a string of
exactly N characters otherwise. The i-th character in y must be C if the i-th activity is assigned to
Loraine in your proposed schedule, and J if it is assigned to Charles
"""

print(f"PROGRAM BEGIN")
print(f"""PLEASE NOTE:
    No error handling is being done. Incorrect inputs will result in a crash
    - Error handling was not a requirement for this exercise
    Assumes only hand input via keyboard - no file handling
    Test cases, number of activites, start and end minutes are assumed to be whole integers
    Answers are output when all test cases are entered. Answers are strings.
""")

answers = list()

carers = ["C", "J"]

T = input("Number of test cases: ")
for i in range (0, int(T)):
    N = input("Number of activities: ")
    activities = list()
    for j in range(0, int(N)):
        S = input("Start and end minutes: ")
        (Si, Ei) = S.split()
        activities.append({
            "id": j,
            "minutes": int(Si)
        })
        activities.append({
            "id": j,
            "minutes": int(Ei)
        })
    # end for j in range (0, N)

    activities.sort(key=lambda e: e["minutes"])
    # activities is now a time line
    # id order is preserved eg: 100(1) < 100(2)

    ans = ""
    seen = {}
    for a in activities:
        if a["id"] in seen:
            carers.append(seen[a["id"]])
        else:
            if len(carers) == 0:
                ans = "IMPOSSIBLE"
                break
            # fi
            a["carer"] = carers.pop()
            ans += a["carer"]
            seen[a["id"]] = a["carer"]
        # fi
    # end for a in activities
    answers.append(ans)
# end for i in range (0, T)

i = 0
for a in answers:
    i += 1
    print(f"Case #{i}: {a}")
# end for a in answers

print(f"PROGRAM COMPLETE")
