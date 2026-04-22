import java.util.ArrayList;
import java.util.Scanner;

// Негізгі класс
public class StudentManager {
    
    // Студент мәліметтерін сақтайтын ішкі класс (Model)
    static class Student {
        private String id;
        private String name;
        private double gpa;

        public Student(String id, String name, double gpa) {
            this.id = id;
            this.name = name;
            this.gpa = gpa;
        }

        public String getId() { return id; }
        
        @Override
        public String toString() {
            return String.format("ID: %s | Аты-жөні: %-15s | GPA: %.2f", id, name, gpa);
        }
    }

    public static void main(String[] args) {
        ArrayList<Student> students = new ArrayList<>();
        Scanner scanner = new Scanner(System.in);
        
        while (true) {
            System.out.println("\n===== СТУДЕНТТЕРДІ БАСҚАРУ ЖҮЙЕСІ =====");
            System.out.println("1. Жаңа студент қосу");
            System.out.println("2. Тізімді көрсету");
            System.out.println("3. ID бойынша іздеу");
            System.out.println("4. Шығу");
            System.out.print("Таңдауыңыз: ");

            int choice = scanner.nextInt();
            scanner.nextLine(); // Жолды тазалау

            if (choice == 1) {
                System.out.print("ID: ");
                String id = scanner.nextLine();
                System.out.print("Аты-жөні: ");
                String name = scanner.nextLine();
                System.out.print("GPA: ");
                double gpa = scanner.nextDouble();
                
                students.add(new Student(id, name, gpa));
                System.out.println("Мәлімет сақталды!");

            } else if (choice == 2) {
                System.out.println("\n--- Студенттер тізімі ---");
                if (students.isEmpty()) {
                    System.out.println("Тізім бос.");
                } else {
                    for (Student s : students) System.out.println(s);
                }

            } else if (choice == 3) {
                System.out.print("Іздеу үшін ID енгізіңіз: ");
                String searchId = scanner.nextLine();
                boolean found = false;
                for (Student s : students) {
                    if (s.getId().equalsIgnoreCase(searchId)) {
                        System.out.println("Табылды: " + s);
                        found = true;
                        break;
                    }
                }
                if (!found) System.out.println("Мұндай студент табылмады.");

            } else if (choice == 4) {
                System.out.println("Жүйеден шығу...");
                break;
            } else {
                System.out.println("Қате таңдау! 1-4 аралығындағы санды таңдаңыз.");
            }
        }
        scanner.close();
    }
}
