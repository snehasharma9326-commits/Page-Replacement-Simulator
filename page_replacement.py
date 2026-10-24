def fifo(pages, capacity):
    frames = []
    pointer = 0
    history = []

    for page in pages:
        if page in frames:
            result = "HIT"
        else:
            result = "FAULT"

            if len(frames) < capacity:
                frames.append(page)
            else:
                frames[pointer] = page
                pointer = (pointer + 1) % capacity

        history.append((page, frames.copy(), result))

    return history


def lru(pages, capacity):
    frames = []
    last_used = {}
    history = []

    for i, page in enumerate(pages):
        if page in frames:
            result = "HIT"
        else:
            result = "FAULT"

            if len(frames) < capacity:
                frames.append(page)
            else:
                old_page = min(frames, key=lambda p: last_used[p])
                frames[frames.index(old_page)] = page

        last_used[page] = i
        history.append((page, frames.copy(), result))

    return history


def optimal(pages, capacity):
    frames = []
    history = []

    for i, page in enumerate(pages):
        if page in frames:
            result = "HIT"
        else:
            result = "FAULT"

            if len(frames) < capacity:
                frames.append(page)
            else:
                future = pages[i + 1:]

                def next_use(p):
                    if p not in future:
                        return float("inf")
                    return future.index(p)

                old_page = max(frames, key=next_use)
                frames[frames.index(old_page)] = page

        history.append((page, frames.copy(), result))

    return history


def display_results(name, history, capacity):
    hits = sum(1 for _, _, result in history if result == "HIT")
    faults = len(history) - hits
    total = len(history)

    print("\n", name, "Page Replacement")
    print("-" * 55)
    print(f"{'Page':<8}{'Frames':<30}{'Result'}")
    print("-" * 55)

    for page, frames, result in history:
        frame_text = " ".join(map(str, frames))
        print(f"{page:<8}{frame_text:<30}{result}")

    hit_ratio = hits / total
    fault_ratio = faults / total

    print("-" * 55)
    print("Total Pages :", total)
    print("Page Hits   :", hits)
    print("Page Faults :", faults)
    print(f"Hit Ratio   : {hit_ratio:.4f} ({hit_ratio * 100:.2f}%)")
    print(f"Fault Ratio : {fault_ratio:.4f} ({fault_ratio * 100:.2f}%)")

    return {
        "hits": hits,
        "faults": faults,
        "hit_ratio": hit_ratio,
        "fault_ratio": fault_ratio
    }


def main():
    print("PAGE REPLACEMENT ALGORITHM SIMULATOR")
    print("=" * 40)

    try:
        pages = list(map(int, input(
            "Enter page reference string (space-separated): "
        ).split()))

        capacity = int(input("Enter number of frames: "))

        if not pages:
            print("Error: Reference string cannot be empty.")
            return

        if capacity <= 0:
            print("Error: Frames must be greater than zero.")
            return

        if any(page < 0 for page in pages):
            print("Error: Page numbers cannot be negative.")
            return

    except ValueError:
        print("Error: Enter valid integers only.")
        return

    algorithms = [
        ("FIFO", fifo(pages, capacity)),
        ("LRU", lru(pages, capacity)),
        ("Optimal", optimal(pages, capacity))
    ]

    summaries = {}

    for name, history in algorithms:
        summaries[name] = display_results(name, history, capacity)

    print("\nPERFORMANCE COMPARISON")
    print("=" * 65)
    print(f"{'Algorithm':<12}{'Hits':<8}{'Faults':<10}"
          f"{'Hit Ratio %':<15}{'Fault Ratio %':<15}")
    print("-" * 65)

    for name, history in algorithms:
        data = summaries[name]
        print(
            f"{name:<12}{data['hits']:<8}{data['faults']:<10}"
            f"{data['hit_ratio'] * 100:<15.2f}"
            f"{data['fault_ratio'] * 100:<15.2f}"
        )

    best = min(
        summaries,
        key=lambda name: summaries[name]["faults"]
    )

    print("\nFewest page faults for this input:", best)
    print("Optimal is a theoretical benchmark using future knowledge.")


if __name__ == "__main__":
    main()