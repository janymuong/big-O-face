# notes — utf-8 validation

**approach:**

**time complexity:**
**space complexity:**

**gotchas / follow-ups:**


## approach

we scan the byte array left to right, keeping a counter `need` that tells us how many **continuation bytes** (of the form `10xxxxxx`) we still expect for the current multi‑byte character.

- When `need == 0`, we are at the start of a new character. We look at the leading bits of the current byte to decide whether it is a 1‑, 2‑, 3‑, or 4‑byte character. If the byte does not match any valid pattern, the encoding is invalid.
- When `need > 0`, we are inside a multi‑byte character. Every byte must start with the bits `10`. If not, the encoding is invalid; otherwise we decrement `need`.
- At the end, we must have `need == 0` (no incomplete character).

Only the **least significant 8 bits** of each integer are used, so we mask each value with `0xFF` before checking.

## time complexity

**O(n)** – we visit each byte exactly once, where `n` is the length of `data`.

## space complexity

**O(1)** – only a constant amount of extra memory is used (the `need` counter).

## gotchas / follow‑ups

- the input integers may have bits beyond the 8th; always mask with `0xFF` to ignore them.
- the leading byte patterns are:
  - `0xxxxxxx` → 1 byte
  - `110xxxxx` → 2 bytes
  - `1110xxxx` → 3 bytes
  - `11110xxx` → 4 bytes
- continuation bytes must always be `10xxxxxx`.
- an overlong encoding (e.g. using a 4‑byte sequence to encode a character that fits in 2 bytes) is **not** considered invalid by this problem – we only check the structural rules.
- the problem guarantees that `1 <= data.length <= 2 * 10^4`, so an O(n) solution easily fits within the time limit.