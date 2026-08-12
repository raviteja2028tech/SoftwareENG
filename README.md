# GitHub Actions – Python CI

A beginner-friendly **Continuous Integration (CI)** workflow for a Python/ML project using GitHub Actions.

## 🚀 What This Project Does

Whenever code is pushed to the `main` branch, GitHub Actions automatically:

1. Sets up **Python 3.10**
2. Installs project dependencies
3. Runs **Pylint** for code-quality checks
4. Runs **Pytest** for automated testing
5. Displays test output in the Actions logs

### 🔄 Workflow

```text
Git Push
   ↓
GitHub Actions
   ↓
Install Dependencies
   ↓
Pylint
   ↓
Pytest
   ↓
Test Results
```

## 🛠️ Tech Stack

* Python
* Git & GitHub
* GitHub Actions
* Pylint
* Pytest
* NumPy
* Pandas
* Scikit-learn

## 🧪 Testing

The project includes a Pytest test that verifies the expected ML prediction.

Example result:

```text
1 passed
```

`pytest -s` is used to display `print()` output in the GitHub Actions logs.

## 📚 What I Learned

* Basics of **CI using GitHub Actions**
* Creating workflows with YAML
* Automated Python testing with Pytest
* Code-quality checking with Pylint
* How GitHub automatically runs checks after a push

## 🔮 Future Improvements

* Fix Pylint warnings
* Add more automated tests
* Add test coverage
* Build a complete CI/CD pipeline

---

**First step toward understanding CI/CD and automated software testing.** 🚀
