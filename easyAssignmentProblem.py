def easyAssignmentProblem(skills):
    return ([1, 2] if skills[0][0] - skills[1][0] >= skills[0][1] - skills[1][1]
        else [2, 1])