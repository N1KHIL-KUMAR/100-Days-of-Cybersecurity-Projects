#!/use/bin/python3


import tkinter as tk
from tkinter import filedialog
import threading
import requests

MAX_THREADS = 20  # Limit max concurrent threads
semaphore = threading.Semaphore(MAX_THREADS)

def gui_interf():
    def find_subdomains():
        domain = entry_sub.get()
        wordlist_path = path_entry.get()
        output_box.delete(1.0, tk.END)
        count_var.set("Found: 0")
        found = []
        threads = []

        try:
            with open(wordlist_path, 'r') as file:
                words = file.read().splitlines()
        except Exception as e:
            output_box.insert(tk.END, f"Error reading file: {e}\n")
            return

        def check_subdomain(word):
            subdomain = f"http://{word}.{domain}"
            try:
                semaphore.acquire()
                response = requests.get(subdomain, timeout=2)
                if response.status_code < 400:
                    found.append(subdomain)
                    output_box.insert(tk.END, f"[+] Found: {subdomain}\n")
                    count_var.set(f"Found: {len(found)}")
            except:
                pass
            finally:
                semaphore.release()

        for word in words:
            t = threading.Thread(target=check_subdomain, args=(word,))
            threads.append(t)
            t.start()

        for t in threads:
            t.join()

        # Save results
        with open("found_subdomains.txt", "w") as f:
            for sub in found:
                f.write(sub + "\n")
        output_box.insert(tk.END, "\nSaved to found_subdomains.txt\n")

    def start_thread():
        threading.Thread(target=find_subdomains, daemon=True).start()

    # GUI setup
    root = tk.Tk()
    root.title("Subdomain Finder GUI")
    root.geometry("400x600")
    root.resizable(False, False) 

    tk.Label(root, text="Target Domain", font=("Arial", 10)).place(x=80, y=10)
    entry_sub = tk.Entry(root)
    entry_sub.insert(0, "google.com")
    entry_sub.place(x=80, y=30, width=250)

    tk.Label(root, text="Wordlist Path", font=("Arial", 10)).place(x=80, y=70)
    path_entry = tk.Entry(root)
    path_entry.place(x=80, y=90, width=250)

    tk.Button(root, text="Browse Wordlist", command=lambda: (
        path_entry.delete(0, tk.END),
        path_entry.insert(0, filedialog.askopenfilename())
    )).place(x=80, y=120, width=250)

    tk.Button(root, text="Start Finding", command=start_thread).place(x=80, y=160, width=250)

    count_var = tk.StringVar(value="Found: 0")
    tk.Label(root, textvariable=count_var, font=("Arial", 10, "bold")).place(x=80, y=200)

    output_box = tk.Text(root, wrap="word")
    output_box.place(x=80, y=230, width=250, height=320)

    root.mainloop()

gui_interf()
