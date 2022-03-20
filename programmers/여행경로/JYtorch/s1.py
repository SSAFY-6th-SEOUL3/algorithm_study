def calc(cur_ticket, tickets, answer, used):
    global result
    if len(answer) == len(tickets) + 1:
        result = answer
        return
    else:
        next_ticket_list = []
        for i in range(len(tickets)):
            ticket = tickets[i]
            if used[i]: continue
            if cur_ticket[1] == ticket[0]:
                next_ticket_list.append((ticket, i))

        if not next_ticket_list: return
        next_ticket_list.sort(key=lambda x:x[0][1])
        for i in range(len(next_ticket_list)):
            next_ticket, next_ticket_idx = next_ticket_list[i]

            used[next_ticket_idx] = 1
            answer.append(next_ticket[1])
            calc(next_ticket, tickets, answer, used)
            if len(result) == len(tickets) + 1: return
            used[next_ticket_idx] = 0
            answer.pop()


def solution(tickets):
    answer = []
    used = [0] * len(tickets)
    first_ticket_list = []

    for i in range(len(tickets)):
        ticket = tickets[i]
        if ticket[0] == 'ICN':
            first_ticket_list.append((ticket, i))

    first_ticket_list.sort(key=lambda x:x[0][1])
    for i in range(len(first_ticket_list)):
        first_ticket, first_ticket_idx = first_ticket_list[i]

        used[first_ticket_idx] = 1
        calc(first_ticket, tickets, [first_ticket[0], first_ticket[1]], used)
        used[first_ticket_idx] = 0
        if len(result) == len(tickets) + 1: return result
    return result


result = []
print(solution([["ICN", "COO"], ["ICN", "BOO"], ["COO", "ICN"]]))
