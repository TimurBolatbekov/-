# -import java.util.ArrayList;
import java.util.Scanner;

public class Main {

    // 🔹 Student class
    static class Student {
        int id;
        String name;
        int age;

        public Student(int id, String name, int age) {
            this.id = id;
            this.name = name;
            this.age = age;
        }

        public void display() {
            System.out.println("ID: " + id + ", Name: " + name + ", Age: " + age);
        }
    }

    // 🔹 Student Manager
    static class StudentManager {
        ArrayList<Student> students = new ArrayList<>();

        public void addStudent(Student s) {
            students.add(s);
            System.out.println("✅ Student added!");
        }

        public void showStudents() {
            if (students.isEmpty()) {
                System.out.println("❌ No students found.");
                return;
            }
            for (Student s : students) {
                s.display();
            }
        }

        public void removeStudent(int id) {
            boolean removed = students.removeIf(s -> s.id == id);
            if (removed) {
                System.out.println("✅ Student removed.");
            } else {
                System.out.println("❌ Student not found.");
            }
        }

        public void findStudent(int id) {
            for (Student s : students) {
                if (s.id == id) {
                    s.display();
                    return;
                }
            }
            System.out.println("❌ Student not found.");
        }
    }

    // 🔹 Main method
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        StudentManager manager = new StudentManager();

        while (true) {
            System.out.println("\n===== Student Management System =====");
            System.out.println("1. Add Student");
            System.out.println("2. Show Students");
            System.out.println("3. Remove Student");
            System.out.println("4. Find Student");
            System.out.println("5. Exit");
            System.out.print("Choose: ");

            int choice = sc.nextInt();

            switch (choice) {
                case 1:
                    System.out.print("Enter ID: ");
                    int id = sc.nextInt();
                    sc.nextLine(); // buffer тазалау

                    System.out.print("Enter Name: ");
                    String name = sc.nextLine();

                    System.out.print("Enter Age: ");
                    int age = sc.nextInt();

                    manager.addStudent(new Student(id, name, age));
                    break;

                case 2:
                    manager.showStudents();
                    break;

                case 3:
                    System.out.print("Enter ID to remove: ");
                    int removeId = sc.nextInt();
                    manager.removeStudent(removeId);
                    break;

                case 4:
                    System.out.print("Enter ID to find: ");
                    int findId = sc.nextInt();
                    manager.findStudent(findId);
                    break;

                case 5:
                    System.out.println("👋 Goodbye!");
                    return;

                default:
                    System.out.println("❌ Invalid choice!");
            }
        }
    }
}
