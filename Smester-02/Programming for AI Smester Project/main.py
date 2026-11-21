# ================================================================
#    AI-BASED GPA PREDICTION AND PERFORMANCE ANALYSIS SYSTEM
# ================================================================
#    Submitted by : Umair Shabbir | Sayyed Abu Bakkar Khan | Musa Khan
#    Reg. IDs : 2502027 | 2502039 | 2502067
#    Course  : Programming for AI
#    Smester   : Second 
#    Section : BS Artificial Intelligence - eve
# ================================================================

import numpy as np               
import matplotlib.pyplot as plt              # Importing the used libraries 
import pandas as pd              
from datetime import datetime    


# Converting marks into grade and points. 

def get_grade_info(mark):
   
    if   mark >= 85: return "A+", 4.0
    elif mark >= 80: return "A",  4.0
    elif mark >= 75: return "A-", 3.7
    elif mark >= 71: return "B+", 3.3
    elif mark >= 68: return "B",  3.0
    elif mark >= 64: return "B-", 2.7
    elif mark >= 61: return "C+", 2.3
    elif mark >= 58: return "C",  2.0
    elif mark >= 54: return "C-", 1.7
    elif mark >= 51: return "D+", 1.3
    elif mark >= 45: return "D",  1.0
    else:            return "F",  0.0


# Header of my project

def print_header():
   
    print("\n" + "=" * 66)
    print("   AI-BASED GPA PREDICTION & PERFORMANCE ANALYSIS SYSTEM")
    print("       Course: Programming for AI  |  BS Artificial Intelligence")
    print("=" * 66)


# Collecting student info

def get_student_info():

    print("\n" + "-" * 66)
    print("  STEP 1: STUDENT INFORMATION INPUT")
    print("-" * 66)

    student_name = input("\n  Enter Student Name      : ").strip()

    while True:
        try:
            num_subjects = int(input("  Enter Number of Subjects: "))
            if num_subjects >= 1:
                break                              
            print("  [!] Must have at least 1 subject.")
        except ValueError:
            print("  [!] Please enter a whole number (e.g., 5).")

    subjects     = []   
    marks_list   = []   
    credits_list = []  

    print("\n  --- Enter Details for Each Subject ---\n")

    for i in range(num_subjects):
        print(f"  Subject {i + 1}:")

        # Subject name
        subj_name = input("    Subject Name     : ").strip()

        # Marks (with verification)
        while True:
            try:
                mark = float(input("    Marks (0-100)    : "))
                if 0.0 <= mark <= 100.0:
                    break
                print("    [!] Marks must be between 0 and 100.")
            except ValueError:
                print("    [!] Please enter a number (e.g., 78.5).")

        # Credit hours (with verification)
        while True:
            try:
                credit = int(input("    Credit Hours     : "))
                if 1 <= credit <= 4:
                    break
                print("    [!] Credit hours must be 1, 2, 3, or 4.")
            except ValueError:
                print("    [!] Please enter a whole number.")

        # Add to lists
        subjects.append(subj_name)
        marks_list.append(mark)
        credits_list.append(credit)
        print()

    # Converting lists to NumPy arrays.
  
    marks_array   = np.array(marks_list,   dtype=float)
    credits_array = np.array(credits_list, dtype=float)

    return student_name, subjects, marks_array, credits_array


# Function to process grades

def process_grades(marks_array):
    
    grades       = []   
    grade_points = []   

    for mark in marks_array:
        grade, points = get_grade_info(mark)   
        grades.append(grade)
        grade_points.append(points)


    grade_points_array = np.array(grade_points, dtype=float)

    return grades, grade_points_array


# Function to calculate GPA

def calculate_gpa(grade_points_array, credits_array):
    

    weighted_sum  = np.dot(grade_points_array, credits_array)

    total_credits = np.sum(credits_array)

    gpa = weighted_sum / total_credits

    return round(float(gpa), 2), int(total_credits)


# Function to predict performance.

def predict_performance(gpa):
   
    if gpa >= 3.5:
        category = "Excellent [***]"
        remark   = "Outstanding! You qualify for the Honor List."
    elif gpa >= 2.5:
        category = "Good [**]"
        remark   = "Well done! Work a bit harder to reach excellence."
    elif gpa >= 1.5:
        category = "Average [*]"
        remark   = "Below expectations. Focus harder on weak subjects."
    else:
        category = "Weak [!]"
        remark   = "At risk. Seek teacher help and attend extra classes."

    return category, remark


# Function to generate suggestions

def generate_suggestions(subjects, marks_array):
   
    suggestions = []

    weak_indices = np.where(marks_array < 60)[0]

    if len(weak_indices) == 0:
        suggestions.append(
            "All subjects have satisfactory marks. Keep up the great work!"
        )
    else:
        for idx in weak_indices:
            mark = marks_array[idx]     
            subj = subjects[idx]        

            if mark < 45:
                tip = "FAILING grade. Urgent revision and teacher help required."
            elif mark < 50:
                tip = "Very close to failing. Solve past exam papers immediately."
            else:
                tip = "Below passing. Review lecture notes and ask questions."

            suggestions.append(
                f"Improve '{subj}' (Marks: {mark:.0f}/100) -- {tip}"
            )

    return suggestions


# Function to perform statistical analysis 

def statistical_analysis(marks_array, subjects):
    
    stats = {
        "Highest Marks"      : float(np.max(marks_array)),
        "Lowest Marks"       : float(np.min(marks_array)),
        "Average Marks"      : float(np.mean(marks_array)),
        "Standard Deviation" : float(np.std(marks_array)),
        "Best Subject"       : subjects[int(np.argmax(marks_array))],
        "Weakest Subject"    : subjects[int(np.argmin(marks_array))],
        "Subjects Above 75"  : int(np.sum(marks_array >= 75)),
        "Subjects Below 60"  : int(np.sum(marks_array < 60)),
    }
    return stats


# Function to display results

def display_results(student_name, subjects, marks_array, credits_array,
                    grades, grade_points_array, gpa, total_credits,
                    performance, remark, suggestions, stats):
   


    print("\n\n" + "=" * 66)
    print("                STUDENT PERFORMANCE REPORT")
    print("=" * 66)
    print(f"  Student Name   : {student_name}")
    print(f"  Report Date    : {datetime.now().strftime('%B %d, %Y  |  %I:%M %p')}")
    print(f"  Total Credits  : {total_credits}")
    print(f"  GPA            : {gpa:.2f} / 4.00")
    print(f"  Performance    : {performance}")
    print(f"  Remark         : {remark}")
    print("=" * 66)

    print("\n  GRADE CARD - SUBJECT-WISE RESULTS\n")

    df = pd.DataFrame({
        "Subject"      : subjects,
        "Marks"        : [f"{m:.1f}" for m in marks_array],
        "Grade"        : grades,
        "Grade Points" : [f"{gp:.1f}" for gp in grade_points_array],
        "Credits"      : credits_array.astype(int),
    })


    df_string = df.to_string(index=False)
    for line in df_string.split('\n'):
        print("  " + line)      

    print("\n\n  STATISTICAL ANALYSIS ")
    print("  " + "-" * 50)
    for key, value in stats.items():
        if isinstance(value, float):
            print(f"  {key:<28} : {value:>7.2f}")
        else:
            print(f"  {key:<28} : {value}")
    print("  " + "-" * 50)

    #  Smart Suggestions 
    print("\n  SMART IMPROVEMENT SUGGESTIONS")
    print("  " + "-" * 62)
    for suggestion in suggestions:
        print(f"    >> {suggestion}")
    print("  " + "-" * 62)

    print("\n" + "=" * 66)


# Function to save results to a file

def save_to_file(student_name, subjects, marks_array, credits_array,
                 grades, grade_points_array, gpa, total_credits,
                 performance, remark, suggestions, stats):

    # Build the filename by name of student 
    filename = student_name.replace(' ', '_') + "_result.txt"

    with open(filename, 'w', encoding='utf-8') as file:


        file.write("=" * 66 + "\n")
        file.write("         AI-BASED GPA PREDICTION - STUDENT RESULT\n")
        file.write("=" * 66 + "\n")
        file.write(f"Student Name   : {student_name}\n")
        file.write(f"Date and Time  : {datetime.now().strftime('%B %d, %Y  |  %I:%M %p')}\n")
        file.write(f"Total Credits  : {total_credits}\n")
        file.write(f"GPA            : {gpa:.2f} / 4.00\n")
        file.write(f"Performance    : {performance}\n")
        file.write(f"Remark         : {remark}\n")
        file.write("=" * 66 + "\n\n")

        # Grade card table
        file.write("GRADE CARD -- SUBJECT-WISE RESULTS\n")
        file.write("-" * 66 + "\n")
        file.write(f"{'Subject':<25} {'Marks':>7} {'Grade':>6} "
                   f"{'Grade Pts':>10} {'Credits':>8}\n")
        file.write("-" * 66 + "\n")
        for i in range(len(subjects)):
            file.write(
                f"{subjects[i]:<25} {marks_array[i]:>7.1f} {grades[i]:>6} "
                f"{grade_points_array[i]:>10.1f} {int(credits_array[i]):>8}\n"
            )
        file.write("-" * 66 + "\n\n")

        # Statistical analysis section
        file.write("STATISTICAL ANALYSIS\n")
        file.write("-" * 50 + "\n")
        for key, value in stats.items():
            if isinstance(value, float):
                file.write(f"{key:<28} : {value:>7.2f}\n")
            else:
                file.write(f"{key:<28} : {value}\n")

        # Suggestions section
        file.write("\nSMART IMPROVEMENT SUGGESTIONS\n")
        file.write("-" * 66 + "\n")
        for s in suggestions:
            file.write(f"  >> {s}\n")

        # Footer
        file.write("\n" + "=" * 66 + "\n")
        file.write("        Generated by AI-Based GPA Prediction System\n")
        file.write("=" * 66 + "\n")

    return filename


# Function to plot graphs

def plot_graphs(subjects, marks_array, gpa, student_name):


    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    fig.patch.set_facecolor('#f8f9fa')  

    fig.suptitle(
        f"Performance Analysis Report  --  {student_name}",
        fontsize=14, fontweight='bold', color='#2c3e50'
    )

    # GRAPH 1: Subject-wise Marks - Color-coded Bar Chart

    bar_colors = [
        '#2ecc71' if m >= 75 else    # Green  for marks >= 75
        '#f39c12' if m >= 60 else    # Orange for marks >= 60
        '#e74c3c'                     # Red    for marks <  60
        for m in marks_array
    ]

    # Draw the bars on ax1 (left panel)
    bars = ax1.bar(
        subjects,          # x-axis: subject names
        marks_array,       # y-axis: marks values
        color=bar_colors,  # bar colors we created above
        edgecolor='white',
        linewidth=1.0,
        width=0.55
    )

    ax1.set_title("Subject-wise Marks", fontsize=12, fontweight='bold', pad=10)
    ax1.set_xlabel("Subjects", fontsize=10)
    ax1.set_ylabel("Marks (out of 100)", fontsize=10)
    ax1.set_ylim(0, 115)              
    ax1.set_facecolor('#f0f4f8')     
    ax1.grid(axis='y', linestyle='--', alpha=0.5, color='#aaaaaa')
    ax1.tick_params(axis='x', rotation=30, labelsize=8)

    # Horizontal reference lines
    ax1.axhline(60, color='#e74c3c', linestyle='--', linewidth=1.2, label='Pass Mark (60)')
    ax1.axhline(75, color='#2ecc71', linestyle='--', linewidth=1.2, label='Good Mark (75)')
    ax1.legend(fontsize=8, loc='lower right')

    # Write the marks value on top of each bar
    for bar, mark in zip(bars, marks_array):
        ax1.text(
            bar.get_x() + bar.get_width() / 2,  
            bar.get_height() + 1.5,             
            f'{mark:.0f}',                      
            ha='center', va='bottom',
            fontsize=9, fontweight='bold', color='#2c3e50'
        )

    # GRAPH 2: GPA Visualization with Performance Zones

    ax2.set_facecolor('#f0f4f8')

    gpa_zones = [
        (0.0, 1.5, '#fde8e8', 'Weak'),
        (1.5, 2.5, '#fef3e2', 'Average'),
        (2.5, 3.5, '#ddeeff', 'Good'),
        (3.5, 4.0, '#e8fde8', 'Excellent'),
    ]

    # Draw each zone as a horizontal background bar
    for start, end, color, label in gpa_zones:
        ax2.barh(
            ['GPA Scale'],          # y-axis category name
            [end - start],          # bar length (zone width)
            left=start,             # where the bar starts on x-axis
            color=color,
            edgecolor='#cccccc',
            linewidth=0.5,
            height=0.35
        )
        # Label in the center of each zone
        ax2.text(
            (start + end) / 2, 0,   
            label,
            ha='center', va='center',
            fontsize=9, color='#555555'
        )

    # Choose bar color based on the student's GPA level
    if   gpa >= 3.5: gpa_color, gpa_label = '#27ae60', 'Excellent'
    elif gpa >= 2.5: gpa_color, gpa_label = '#2980b9', 'Good'
    elif gpa >= 1.5: gpa_color, gpa_label = '#e67e22', 'Average'
    else:            gpa_color, gpa_label = '#c0392b', 'Weak'

    # Draw the student's GPA bar (on top of the zones)
    ax2.barh(
        ['Your GPA'],   
        [gpa],          
        color=gpa_color,
        edgecolor='black',
        linewidth=1,
        height=0.35
    )

    # GPA value label next to the bar
    ax2.text(
        gpa + 0.07, 1,          
        f'{gpa:.2f}',           
        va='center', fontsize=13,
        fontweight='bold', color=gpa_color
    )

    # Chart labels and grid
    ax2.set_xlim(0, 4.4)
    ax2.set_title(
        f"GPA: {gpa:.2f} / 4.00  |  {gpa_label}",
        fontsize=12, fontweight='bold', pad=10
    )
    ax2.set_xlabel("Grade Points (0.0 - 4.0)", fontsize=10)
    ax2.grid(axis='x', linestyle='--', alpha=0.4)

    # ---- Save and display the charts ----
    plt.tight_layout(pad=2.5)

    chart_filename = "performance_chart.png"
    plt.savefig(chart_filename, dpi=150, bbox_inches='tight')  # Save to disk first
    plt.show()                                                  # Then show on screen

    return chart_filename


# ================================================================
# MAIN FUNCTION ---
# ================================================================

def main():

    # Step 1: Display the program title banner
    print_header()

    # Step 2: Collect student name, subjects, marks, and credit hours
    student_name, subjects, marks_array, credits_array = get_student_info()

    # Step 3: Convert each mark to a grade letter and grade points
    grades, grade_points_array = process_grades(marks_array)

    # Step 4: Calculate GPA using NumPy dot product and sum
    gpa, total_credits = calculate_gpa(grade_points_array, credits_array)

    # Step 5: Classify student performance (AI / rule-based classifier)
    performance, remark = predict_performance(gpa)

    # Step 6: Find weak subjects and generate improvement suggestions
    suggestions = generate_suggestions(subjects, marks_array)

    # Step 7: Compute statistics using NumPy functions
    stats = statistical_analysis(marks_array, subjects)

    # Step 8: Display the full formatted report in terminal
    display_results(
        student_name, subjects, marks_array, credits_array,
        grades, grade_points_array, gpa, total_credits,
        performance, remark, suggestions, stats
    )

    # Step 9: Save the complete report to a text file automatically
    filename = save_to_file(
        student_name, subjects, marks_array, credits_array,
        grades, grade_points_array, gpa, total_credits,
        performance, remark, suggestions, stats
    )
    print(f"\n  [OK] Report saved as  : '{filename}'")

    # Step 10: Generate and save performance charts
    print("  [..] Generating performance charts, please wait...")
    chart_file = plot_graphs(subjects, marks_array, gpa, student_name)
    print(f"  [OK] Chart saved as   : '{chart_file}'")

    # Completion message
    print("\n" + "=" * 66)
    print("  [DONE] Analysis complete! Thank you for using the system.")
    print("=" * 66 + "\n")


# ================================================================
# PROGRAM ENTRY POINT
# ================================================================
if __name__ == "__main__":
    main()