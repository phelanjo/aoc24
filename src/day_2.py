# ==================
# Part 1
# ==================
def convert_report_to_list(report: str) -> list:
    report_list = []
    for element in report.split():
        report_list.append(int(element))

    return report_list

def is_valid_report(report: list) -> bool:
    for idx, val in enumerate(report):
        is_all_ascending_or_descending = False
        is_within_1_to_3_difference = False

        if idx == 0:
            if val > report[idx+1]:
                # Desdending Order
                if sorted(report, reverse=True) != report:
                    return False
            elif val < report[idx+1]:
                # Ascending Order
                if sorted(report) != report:
                    return False
        
        is_all_ascending_or_descending = True

        if idx < len(report) - 1:
            if 1 <= (abs(val - report[idx+1])) <= 3:
                is_within_1_to_3_difference = True
        else:
            # Since this is the last element in the list, the flag is set to True
            # to avoid an IndexError
            is_within_1_to_3_difference = True

        if not all([is_all_ascending_or_descending, is_within_1_to_3_difference]):
            return False
    
    return True

def get_number_of_valid_reports():
    with open("inputs/day_2_input.txt") as f:
        data = f.readlines()
        
        valid_reports_count = 0
        for report in data:
            report_list = convert_report_to_list(report)
            
            if is_valid_report(report_list):
                valid_reports_count += 1

        return valid_reports_count
    
# ==================
# Part 2 - WIP
# ==================
def is_valid_dampened_report(report: list) -> bool:
    for idx, val in enumerate(report):
        is_all_ascending_or_descending = False
        is_within_1_to_3_difference = False

        # Remove one element from list to see if all checks pass
        sliced_report = report.copy()
        sliced_report.pop(idx)
        print(sliced_report)

        # iterate through the rest of the list and check if the report is now valid
        for sliced_idx, sliced_val in enumerate(sliced_report):
            if sliced_idx == 0:
                if sliced_val > sliced_report[sliced_idx+1]:
                    # Desdending Order
                    if sorted(sliced_report, reverse=True) != sliced_report:
                        is_all_ascending_or_descending = False
                elif sliced_val < sliced_report[sliced_idx+1]:
                    # Ascending Order
                    if sorted(sliced_report) != sliced_report:
                        is_all_ascending_or_descending = False
            
            is_all_ascending_or_descending = True

            if sliced_idx < len(sliced_report) - 1:
                if 1 <= (abs(sliced_val - sliced_report[sliced_idx+1])) <= 3:
                    is_within_1_to_3_difference = True
            else:
                # Since this is the last element in the list, the flag is set to True
                # to avoid an IndexError
                is_within_1_to_3_difference = True

            if not all([is_all_ascending_or_descending, is_within_1_to_3_difference]):
                return False
        
        is_all_ascending_or_descending = True

        if idx < len(report) - 1:
            if 1 <= (abs(val - report[idx+1])) <= 3:
                is_within_1_to_3_difference = True
        else:
            # Since this is the last element in the list, the flag is set to True
            # to avoid an IndexError
            is_within_1_to_3_difference = True

        if not all([is_all_ascending_or_descending, is_within_1_to_3_difference]):
            return False
    
    return True

def get_number_of_valid_reports__with_dampener():
    with open("inputs/day_2_input.txt") as f:
        data = f.readlines()
        
        valid_reports_count = 0
        for report in data:
            report_list = convert_report_to_list(report)
            
            if is_valid_dampened_report(report_list):
                valid_reports_count += 1

        return valid_reports_count