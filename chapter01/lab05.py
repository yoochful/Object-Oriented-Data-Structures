# Chapter : 1 - item : 5 - vickrey auction# จงสร้าง vickrey auction แบบจำลอง

# Vickrey auction คือการประมวลที่ผู้ที่จะชนะการประมูล คือ ผู้ที่ยื่นซองเสนอราคาสูงที่สุด แต่จะจ่ายจริงในราคาที่สูงเป็นอันดับสองรองลงมา

# word
# รับค่าโดย "Enter All Bid : "
# ถ้ามีน้อยกว่า 2 จำนวน ให้แสดงข้อความ "not enough bidder"
# ถ้ามี 2 จำนวนเท่ากัน ให้แสดงข้อความ "error : have more than one highest bid"
# ถ้ามีผู้ชนะให้แสดง "winner bid is $ need to pay $"

# Test case 1 
# Enter All Bid : 5
# not enough bidder

# Test case 2
# Enter All Bid : 5 10 20 5 16
# winner bid is 20 need to pay 16

# Test case 3
# Enter All Bid : 5 10 20 20 10
# error : have more than one highest bid

bids_input = input("Enter All Bid: ").split()
bids = [int(bid) for bid in bids_input]

def vickrey_auction(bids):
    
    not_repeat_bids = list(set(bids))
    
    if len(not_repeat_bids) < 2:
        return "not enough bidder"
    
    highest_bid = max(not_repeat_bids)
    not_repeat_bids.remove(highest_bid)
    
    if bids.count(highest_bid) > 1:
        return "error : have more than one highest bid"
    
    second_highest_bid = max(not_repeat_bids)
    return f"winner bid is {highest_bid} need to pay {second_highest_bid}"

result = vickrey_auction(bids)
print(result)


