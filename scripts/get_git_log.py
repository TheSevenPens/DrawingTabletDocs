import subprocess

out = subprocess.check_output(
    ['git', 'log', '-p', '-n', '5', 'recommendations/pen-tablet-recs/pen-tablet-recs-large.md'],
    cwd=r'c:\Users\seven\Documents\GitHub\DrawingTabletDocs'
)
with open('c:\\Users\\seven\\Documents\\GitHub\\DrawingTabletDocs\\recent_log_clean.txt', 'wb') as f:
    f.write(out)
