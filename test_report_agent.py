from agents.report_agent import report_agent

print("===== EXECUTIVE SUMMARY =====")
print(report_agent("Generate executive summary"))

print("\n" + "=" * 60 + "\n")

print("===== GENERATE REPORT =====")
print(report_agent("Generate report for INC0005"))

print("\n" + "=" * 60 + "\n")

print("===== SEARCH REPORTS =====")
print(report_agent("Show all reports"))