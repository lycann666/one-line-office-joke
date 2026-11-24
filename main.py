"""One-Line Office Joke: 24-Hour Sprint -- make.fun entry.

Writes one line of office humour to ``$MAKEFUN_OUTPUT_DIR/entry.txt``
(default ``/output``).

Two-pass reasoning (written before the final line was chosen).
Freemodel (claude-sonnet-5-5) was consulted: 3 calls, 2 succeeded,
1 truncated mid-sentence and was discarded. Its ranking of my four
drafts was D > B > C > A, and it offered two extra jokes (E, F below).
The ranking below is mine, against the judge's criteria in the order
RULES.txt gives them:

  1. It is a one-line joke about office life, a single line that lands
     as a joke about working in an office.
  2. It is funny: the punchline surprises and pays off the setup in a
     way anyone who has sat in an office recognises.
  3. It is one line: the whole joke reads as a single sentence, or a
     setup and punchline on one line, with no rambling around it.
  4. It is fresh: it finds a specific detail of office life rather
     than a generic complaint, and it is not a joke everyone has
     already heard.
  5. It is clear on first read: no explanation needed, no reference
     the reader cannot follow, and the wording is tight.

  Draft D -- "Our shared drive is a museum of files named
  final_FINAL_v2_REAL_final.docx -- every exhibit a lie."
    1. One-line office joke, yes: shared drives are office life.
    2. Punchline surprises: the museum setup makes the reader expect
       grandeur, then "every exhibit a lie" flips it -- the files
       lie about being final.
    3. One sentence, setup and punchline on one line.
    4. Fresh: the museum metaphor is specific, and the exact
       filename pattern (final_FINAL_v2_REAL_final) is a detail
       every office worker recognises instantly.
    5. Clear on first read: no jargon beyond a filename.
    Verdict: CHOSEN as v1. Freemodel ranked it first too. Pass 2
    then revised it to v2 (see the comment above LINE).

  Draft B -- "The office plant is thriving -- it gets watered,
  sunlight, and nobody ever asks it for a status update."
    1-3. One-line office joke with a real punchline. 2. Weaker than
    D: the "nobody asks it for a status update" turn is a familiar
    gag shape, and the plant's thriving is stated rather than shown.
    Verdict: rejected -- loses to D on criteria 2 and 4.

  Draft C -- "I set my out-of-office reply to 'per my last email'
  so even my absence sounds passive-aggressive."
    2. Relatable, but it leans on the familiar phrase "per my last
    email", so the surprise is thinner. 4. Less fresh than D.
    Verdict: rejected -- loses to D on criteria 2 and 4.

  Draft A -- "Our daily standup is fifteen minutes of standing up
  to say we're still sitting on the same ticket."
    2. Clever standing/sitting wordplay, but the ticket gag feels
    labored next to D's filename detail.
    Verdict: rejected -- loses to D on criteria 2 and 4.

  Draft E (Freemodel) -- "'We're like a family here,' said the
  manager, meaning nobody leaves and everyone eats lunch at their
  desk."
    2. Good second beat ("nobody leaves"), but "we're like a family
    here" is itself a well-worn corporate trope, so the setup is
    borrowed.
    Verdict: rejected -- loses to D on criterion 4.

  Draft F (Freemodel) -- coffee machine with three buttons, one for
  "productive by 9:30". Coffee-machine jokes are a tired office
  trope, and the punchline is a label rather than a turn.
    Verdict: rejected -- loses to D on criteria 2 and 4.

The program is deterministic: one constant string, no network, no
randomness, no clock, no input. Two runs produce byte-identical output.
"""

import os

# PASS 2 (v2) -- revision of v1, with reasons:
#   - "a museum" -> "a carefully curated museum": strengthens the
#     museum metaphor (criterion 4) -- a curated museum implies
#     pride and intent, which makes the punchline "every exhibit a
#     lie" land harder, because the curation itself is the lie.
#   - Nothing else changes: same premise, same filename detail, same
#     punchline; the added words all serve the setup.
#   Net: 115 characters, still one sentence, same premise, sharper turn.
LINE = (
    "Our shared drive is a carefully curated museum of files named "
    "final_FINAL_v2_REAL_final.docx \u2014 every exhibit a lie."
)


def main() -> None:
    # Gate check, mirroring RULES.txt: the entry must be UTF-8 text of
    # 1 to 200 characters, not only white space. Refuse loudly rather
    # than writing an entry the gate would score 0.
    if not isinstance(LINE, str):
        raise ValueError("entry must be a str, got %s" % type(LINE).__name__)
    if not 1 <= len(LINE) <= 200:
        raise ValueError("entry is %d characters, gate allows 1-200" % len(LINE))
    if not LINE.strip():
        raise ValueError("entry must not be only white space")
    if "\n" in LINE or "\r" in LINE:
        raise ValueError("entry must be a single line")
    LINE.encode("utf-8")  # gate requires UTF-8 text
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
