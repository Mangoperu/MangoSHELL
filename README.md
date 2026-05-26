# 🥭 MangoSHELL 

> **A lightweight, UNIX-like command-line interpreter built from scratch in Python.** > *No abstractions. No bloat. Just direct OS-level execution.*

MangoSHELL isn't just a wrapper; it’s a fully functional Read-Eval-Print-Loop (REPL) environment. It strips away standard Python libraries to interact directly with the operating system’s core, handling raw input tokenization, environment variable parsing, and native system calls.

Built for speed, readability, and a deep understanding of systems architecture. 

---

## ✨ Features (TL;DR)

* **$O(1)$ Command Routing:** Ditch the endless `if/else` walls. MangoSHELL uses the Command Pattern via dynamic dictionary mapping for instant built-in execution. 
* **OS-Agnostic `PATH` Parsing:** Seamlessly rips through system environment variables to locate external binaries. Dynamically adapts to Windows (`;`) or POSIX (`:`) separators.
* **Bulletproof Tokenization:** Safely parses heavy, whitespace-riddled user inputs without crashing, bypassing the fragility of standard string slicing.
* **Native Built-ins:** Fast, internal support for core commands (`echo`, `type`, `exit`).
* **Silent Commenting:** Native support for `#` inline comments without disrupting the execution pipeline.

---

## 🧠 Under the Hood (Technical Specs)

This shell was engineered to demonstrate a deep understanding of how software bridges the gap between user intent and hardware execution.

* **`sys` Integration:** Handles standard I/O stream manipulation and raw process exiting.
* **`os` Module Mastery:** Directly queries the kernel for environment variables and validates hardware-level file permissions (`os.X_OK`) before attempting execution.
* **Memory & Buffer Safety:** Explicitly flushes standard output streams to prevent terminal desync and phantom inputs.

---

## 🚀 Quick Start

Drop into the shell and start executing in under 10 seconds.

```bash
# Clone the repo
git clone [https://github.com/yourusername/MangoSHELL.git](https://github.com/yourusername/MangoSHELL.git)

# Navigate to the directory
cd MangoSHELL

# Boot the shell
python main.py# MangoSHELL