#include <iostream>
#include <string>
#include <iomanip>
using namespace std;

const int MAX_BOOKS = 100;


// -- BASE CLASS ------------------------------------------------
class LibraryItem {
protected:
    int    bookID;
    string title;
    string author;

public:
    LibraryItem() : bookID(0), title("N/A"), author("N/A") {}

    LibraryItem(int id, const string& t, const string& a)
        : bookID(id), title(t), author(a) {
    }

    virtual ~LibraryItem() {}

    int    getBookID() const { return bookID; }
    string getTitle()  const { return title; }
    string getAuthor() const { return author; }

    void setTitle(const string& t) { if (!t.empty()) title = t; }
    void setAuthor(const string& a) { if (!a.empty()) author = a; }

    virtual void   display() const = 0;
    virtual string getType() const = 0;
};


// -- DERIVED CLASS ---------------------------------------------
class Book : public LibraryItem {
private:
    int quantity;
    int issuedCount;

public:
    Book() : LibraryItem(), quantity(0), issuedCount(0) {}

    Book(int id, const string& t, const string& a, int qty)
        : LibraryItem(id, t, a), quantity(qty), issuedCount(0) {
    }

    int getQuantity()    const { return quantity; }
    int getIssuedCount() const { return issuedCount; }
    int getAvailable()   const { return quantity - issuedCount; }

    void setQuantity(int q) {
        if (q > 0) quantity = q;
        else cout << "  [!] Quantity must be greater than 0.\n";
    }

    bool issueBook() {
        if (getAvailable() > 0) { issuedCount++; return true; }
        return false;
    }

    bool returnBook() {
        if (issuedCount > 0) { issuedCount--; return true; }
        return false;
    }

    string getType() const override { return "Book"; }

    void display() const override {
        string status = (getAvailable() > 0) ? "Available" : "Not Available";
        cout << "  Type       : " << getType() << "\n"
            << "  Book ID    : " << bookID << "\n"
            << "  Title      : " << title << "\n"
            << "  Author     : " << author << "\n"
            << "  Total Qty  : " << quantity << "\n"
            << "  Issued     : " << issuedCount << "\n"
            << "  Available  : " << getAvailable() << "\n"
            << "  Status     : " << status << "\n";
    }
};


// -- LIBRARY MANAGER -------------------------------------------
class LibraryManager {
private:
    Book* books[MAX_BOOKS];
    int   count;
    static int nextID;

    void printLine(char c = '-', int w = 55) const {
        for (int i = 0; i < w; i++) cout << c;
        cout << "\n";
    }

    int findIndex(int id) const {
        for (int i = 0; i < count; i++)
            if (books[i]->getBookID() == id) return i;
        return -1;
    }

public:
    LibraryManager() : count(0) {
        for (int i = 0; i < MAX_BOOKS; i++)
            books[i] = NULL;
    }

    ~LibraryManager() {
        for (int i = 0; i < count; i++)
            delete books[i];
    }

    void addBook() {
        if (count >= MAX_BOOKS) {
            cout << "\n  [!] Library is full.\n";
            return;
        }
        string title, author;
        int qty;

        cout << "\n";
        printLine('=');
        cout << "              ADD NEW BOOK\n";
        printLine('=');
        cout << "  Enter Title    : "; cin.ignore(); getline(cin, title);
        cout << "  Enter Author   : "; getline(cin, author);
        cout << "  Enter Quantity : "; cin >> qty;

        if (title.empty() || author.empty()) {
            cout << "\n  [!] Title and Author cannot be empty.\n";
            return;
        }
        if (qty <= 0) {
            cout << "\n  [!] Quantity must be at least 1.\n";
            return;
        }

        books[count] = new Book(nextID, title, author, qty);
        cout << "\n  [OK] Book added! Book ID = " << nextID << "\n";
        count++;
        nextID++;
    }

    void displayAll() const {
        if (count == 0) {
            cout << "\n  [!] No books in the library.\n";
            return;
        }
        cout << "\n";
        printLine('=');
        cout << "         ALL BOOKS  (Total: " << count << ")\n";
        printLine('=');
        for (int i = 0; i < count; i++) {
            books[i]->display();
            printLine();
        }
    }

    void searchByID() const {
        int id;
        cout << "\n  Enter Book ID : "; cin >> id;
        int idx = findIndex(id);
        if (idx == -1) {
            cout << "\n  [!] Book with ID " << id << " not found.\n";
            return;
        }
        cout << "\n";
        printLine();
        cout << "             BOOK FOUND\n";
        printLine();
        books[idx]->display();
        printLine();
    }

    void issueBook() {
        int id;
        cout << "\n  Enter Book ID to Issue : "; cin >> id;
        int idx = findIndex(id);
        if (idx == -1) { cout << "\n  [!] Book not found.\n"; return; }

        if (books[idx]->issueBook()) {
            cout << "\n  [OK] Book issued successfully!\n";
            cout << "  Copies Remaining : " << books[idx]->getAvailable() << "\n";
        }
        else {
            cout << "\n  [!] No copies available to issue.\n";
        }
    }

    void returnBook() {
        int id;
        cout << "\n  Enter Book ID to Return : "; cin >> id;
        int idx = findIndex(id);
        if (idx == -1) { cout << "\n  [!] Book not found.\n"; return; }

        if (books[idx]->returnBook()) {
            cout << "\n  [OK] Book returned successfully!\n";
            cout << "  Copies Now Available : " << books[idx]->getAvailable() << "\n";
        }
        else {
            cout << "\n  [!] No issued copies to return.\n";
        }
    }

    void deleteBook() {
        int id;
        cout << "\n  Enter Book ID to Delete : "; cin >> id;
        int idx = findIndex(id);
        if (idx == -1) { cout << "\n  [!] Book not found.\n"; return; }

        cout << "\n  Deleting: \"" << books[idx]->getTitle() << "\"...\n";
        delete books[idx];

        for (int i = idx; i < count - 1; i++)
            books[i] = books[i + 1];

        books[count - 1] = NULL;
        count--;
        cout << "  [OK] Book deleted successfully!\n";
    }
};

int LibraryManager::nextID = 101;


// -- MAIN ------------------------------------------------------
int main() {
    cout << "\n";
    cout << "  +======================================================+\n";
    cout << "  |                                                      |\n";
    cout << "  |         LIBRARY  MANAGEMENT  SYSTEM                  |\n";
    cout << "  |         Developed in C++ (OOP Project)               |\n";
    cout << "  |                                                      |\n";
    cout << "  +======================================================+\n";
    cout << "\n  Welcome! Please choose an option from the menu.\n";

    LibraryManager lib;
    int choice;

    do {
        cout << "\n";
        cout << "  +----------------------------------------------+\n";
        cout << "  |       LIBRARY MANAGEMENT SYSTEM              |\n";
        cout << "  +----------------------------------------------+\n";
        cout << "  |  [1]  Add New Book                           |\n";
        cout << "  |  [2]  Display All Books                      |\n";
        cout << "  |  [3]  Search Book by ID                      |\n";
        cout << "  |  [4]  Issue Book                             |\n";
        cout << "  |  [5]  Return Book                            |\n";
        cout << "  |  [6]  Delete Book                            |\n";
        cout << "  |  [0]  Exit                                   |\n";
        cout << "  +----------------------------------------------+\n";
        cout << "  Enter your choice : ";
        cin >> choice;

        switch (choice) {
        case 1: lib.addBook();    break;
        case 2: lib.displayAll(); break;
        case 3: lib.searchByID(); break;
        case 4: lib.issueBook();  break;
        case 5: lib.returnBook(); break;
        case 6: lib.deleteBook(); break;
        case 0:
            cout << "\n  Thank you for using Library Management System!\n";
            cout << "  Goodbye!\n\n";
            break;
        default:
            cout << "\n  [!] Invalid choice. Enter 0 to 6.\n";
        }
    } while (choice != 0);

    return 0;
}
