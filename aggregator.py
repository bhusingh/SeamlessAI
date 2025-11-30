def simple_merge(responses):
    # For MVP, just concatenate
    merged = "\n\n".join([f"Source {i+1}:\n{resp}" for i, resp in enumerate(responses)])
    return merged
