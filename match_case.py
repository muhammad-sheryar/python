#Python Match-Case -> ALternative of else-if

# def day_of_Week(day):
#      match day:
#         case 1:
#             return "It is Sunday"
#         case 2:
#             return "It is Monday"
#         case 3:
#             return "It is Tuesday"
#         case 4:
#             return "It is Wednesday"
#         case 5:
#             return "It is Thursday"
#         case 6:
#             return "It is Friday"
#         case 7:
#             return "It is Saturday"
        
# print(day_of_Week(1))

# def day_of_Week(day):
#      match day:
#         case "Sunday":
#             return True
#         case "Monday":
#             return False
#         case "Tuesday":
#             return False
#         case "Wednesday":
#             return False
#         case "Thursday":
#             return False
#         case "Friday":
#             return False
#         case "Saturday":
#             return False
        
# print(day_of_Week("Sunday"))


def day_of_Week(day):
     match day:
        case "Sunday"| "Saturday":
            return True
        case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday" | "Saturday":
            return False
        
        
print(day_of_Week("Monday"))