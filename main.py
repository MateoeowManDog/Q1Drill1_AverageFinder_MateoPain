from js import document

def show_result(event=None):
    try:
        s1 = float(document.getElementById("score1").value)
        s2 = float(document.getElementById("score2").value)
        if not (0 <= s1 <= 100 and 0 <= s2 <= 100):
            raise ValueError
        avg = (s1 + s2) / 2
        msg = f"Average Score: {avg:.2f} {'✅ Passed' if avg >= 75 else '❌ Failed'}"
    except:
        msg = "Enter valid numbers (0-100)."
    document.getElementById("result").innerHTML = msg