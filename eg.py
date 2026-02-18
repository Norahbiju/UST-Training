import os
import re
from collections import Counter
LOG_FILE = "app.log"
MIN_WORD_LENGTH = 4
RARE_THRESHOLD = 2  

def clean_and_tokenize(text):
   words = re.findall(r'\b[a-zA-Z]{%d,}\b' % MIN_WORD_LENGTH, text.lower())
   return words

def analyze_log(file_path):
   if not os.path.exists(file_path):
       print("Log file not found.")
       return
   with open(file_path, "r", encoding="utf-8") as file:
       lines = file.readlines()
  
   all_words = []
   for line in lines:
       all_words.extend(clean_and_tokenize(line))
 
   word_counts = Counter(all_words)
   
   rare_words = {word for word, count in word_counts.items() if count <= RARE_THRESHOLD}
   
   anomalous_lines = []
   for line in lines:
       words = clean_and_tokenize(line)
       if any(word in rare_words for word in words):
           anomalous_lines.append(line.strip())
  
   print("========= LOG ANOMALY REPORT =========")
   print(f"Total Lines: {len(lines)}")
   print(f"Total Unique Words: {len(word_counts)}")
   print(f"Rare Words Detected: {len(rare_words)}")
   print(f"Potential Anomalous Lines: {len(anomalous_lines)}")
   print("\n--- Sample Rare Words ---")
   print(list(rare_words)[:10])
   print("\n--- Sample Anomalous Lines ---")
   for line in anomalous_lines[:5]:
       print(line)

if __name__ == "__main__":
   analyze_log(LOG_FILE)