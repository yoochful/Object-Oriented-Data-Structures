if len(bids) < 2:
    print("not enough bidder")

unique_bids = list(set(bids))
unique_bids.sort(reverse=True)

if bids.count(unique_bids[0]) > 1:
    return "error : have more than one highest bid"

highest_bid = unique_bids[0]
second_highest_bid = unique_bids[1]

return f"winner bid is {highest_bid} need to pay {second_highest_bid}"