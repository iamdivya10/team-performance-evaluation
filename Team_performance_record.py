class Team:
    def __init__(self, employee_name, employee_id, employee_role, outcome_review, action):
        self.employee_name = employee_name
        self.employee_id = employee_id
        self.employee_role = employee_role
        self.outcome_review = outcome_review
        self.action = action
        self.performance_rating = None
class EvaluationRecord:

    def __init__(self):
        self.records = []
    def create_evaluation_record(self, employee_name, employee_id, employee_role, outcome_review, performance_rating, action):
        self.records.append({"employee_name": employee_name, "employee_id": employee_id, "employee_role": employee_role,"outcome_review": outcome_review, "performance_rating": performance_rating, "action": action})
        print("Evaluation record created successfully.")
    def list_record(self):
        if self.records:
            print("Team Members:")
            for record in self.records:
                print(f"employee_name:{record['employee_name']},employee_id:{record['employee_id']},employee_role:{record['employee_role']},outcome_review:{record['outcome_review']},performance_rating:{record['performance_rating']},action:{record['action']}")
    def read_records(self, employee_name):
        found_records = [record for record in self.records if record["employee_name"] == employee_name]
        if found_records:
            print(f"Evaluation records for team '{employee_name}':")
            for record in found_records:
                print(f"employee_name:{record['employee_name']},employee_id:{record['employee_id']},employee_role:{record['employee_role']},outcome_review: {record['outcome_review']}, Action: {record['action']},performance_rating:{record['performance_rating']}")
        else:
            print("No evaluation records found for this team.")
    def update_record(self, employee_name, employee_id, employee_new_role, new_outcome_review, new_performance_rating,new_action):
        for record in self.records:
            if record["employee_name"] == employee_name:
                if record["employee_id"] == employee_id:
                    record["employee_role"] = employee_new_role
                    record["outcome_review"] = new_outcome_review
                    record["performance_rating"] = new_performance_rating
                    record["action"] = new_action
                    print("Evaluation record updated successfully.")
                    return
        print("No evaluation records found for this team.")

    def delete_record(self, employee_name, employee_id):
        for record in self.records:
            if record["employee_name"] == employee_name:
                if record["employee_id"] == employee_id:
                    self.records.remove(record)
                    print(f"{employee_name} has been removed from the team.")
                    return
        print(f"record {employee_name} not found.")
    def delete_low_performance_records(self, threshold_rating):
        deleted_records = []
        for record in self.records:
            performance_rating = record.get("performance_rating")
            if performance_rating is not None and (performance_rating) < threshold_rating:
                deleted_records.append(record)
        if deleted_records:
            self.records = [record for record in self.records if record not in deleted_records]
            print("Deleted records with Low Performance Ratings:")
            for record in deleted_records:
                print(f"Name: {record['employee_name']}, id: {record['employee_id']}, Role: {record['employee_role']},outcome_review: {record['outcome_review']}, Action: {record['action']},Performance_rating: {record['performance_rating']}")
        else:
            print("No records with low performance ratings found.")
def main():
    evaluation_record = EvaluationRecord()
    while True:
        print("\n1. Create Evaluation Record")
        print("2. Read Evaluation Records")
        print("3. Update Evaluation Record")
        print("4. List of Evaluation Records")
        print("5. Delete Evaluation Records")
        print("6. Delete low performance rating")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            employee_name = input("Enter member name to add: ")
            employee_id = input("Enter member id to add: ")
            employee_role = input("Enter member role to add: ")
            outcome_review = input("Enter outcome of the review: ")
            performance_rating = float(input(f"Enter performance ratings for {employee_name} :"))
            action = input("Enter action to be taken: ")
            evaluation_record.create_evaluation_record(employee_name, employee_id, employee_role, outcome_review, performance_rating, action)

        elif choice == "2":
            employee_name = input("Enter name to read evaluation records: ")
            employee_id = input("Enter member id to read evaluation records: ")
            evaluation_record.read_records(employee_name)

        elif choice == '3':
            employee_name = input("Enter member's name: ")
            employee_id = input("Enter member's id : ")
            employee_new_role = input("Enter new member role to add: ")
            new_outcome_review = input("Enter new outcome of the review: ")
            new_performance_rating = float(input("Enter new performance rating"))
            new_action = input("Enter new action: ")
            evaluation_record.update_record(employee_name, employee_id, employee_new_role, new_outcome_review, new_action,new_performance_rating)

        elif choice == '4':
            evaluation_record.list_record()

        elif choice == '5':
            employee_name = input("Enter member's name to remove: ")
            employee_id = input("Enter member's id to remove: ")
            evaluation_record.delete_record(employee_name,employee_id)

        elif choice == '6':
            threshold = float(input("\nEnter the threshold rating for deleting low performing members: "))
            evaluation_record.delete_low_performance_records(threshold)

        elif choice == '7':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()
