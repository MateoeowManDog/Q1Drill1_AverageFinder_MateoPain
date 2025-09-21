from pyscript import document

def find_average(event=None):
    s1 = int(document.getElementById("score1").value or 0)
    s2 = int(document.getElementById("score2").value or 0)

    avg = (s1 + s2) / 2
    msg = f"Average: {avg:.2f} ✅ Passed" if avg >= 75 else f"Average: {avg:.2f} ❌ Failed"

    document.getElementById("result").innerHTML = msg
