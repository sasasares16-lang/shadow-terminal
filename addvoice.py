from pathlib import Path

p = Path("www/index.html")
s = p.read_text()
backup = Path("www/index.html.backup")
backup.write_text(s)

if "function scaryVoice()" in s:
    print("كود الصوت موجود مسبقًا.")
elif "</body>" not in s:
    print("لم أجد نهاية الصفحة.")
else:
    code = """
<script>
(function () {
  let played = false;
  function scaryVoice() {
    if (played) return;
    played = true;
    if (!window.speechSynthesis) return;

    function speak(text, pitch, rate) {
      return new Promise(resolve => {
        const msg = new SpeechSynthesisUtterance(text);
        msg.lang = 'en-US';
        msg.pitch = pitch;
        msg.rate = rate;
        msg.volume = 1;
        msg.onend = resolve;
        msg.onerror = resolve;
        speechSynthesis.speak(msg);
      });
    }

    speak('Nega, you got hacked!', 0.65, 0.85)
      .then(() => new Promise(resolve => setTimeout(resolve, 500)))
      .then(() => speak('Hahahahahaha!', 0.5, 0.8));
  }

  document.addEventListener('click', scaryVoice, { once: true });
})();
</script>
"""
    s = s.replace("</body>", code + "\n</body>", 1)
    p.write_text(s)
    print("تمت إضافة الصوت بنجاح.")
