def player(prev_play, opponent_history=[]):
    import random

    # Append the opponent's last move to their history
    if prev_play != '':
        opponent_history.append(prev_play)

    # Initialize the play_order dictionary to store sequences
    if not hasattr(player, 'play_order'):
        player.play_order = {}

    ideal_response = {'P': 'S', 'R': 'P', 'S': 'R'}
    n = 3  # Length of the sequence to consider

    # Build a sequence string of the last (n-1) moves
    if len(opponent_history) >= n:
        seq = ''.join(opponent_history[-(n-1):])
    else:
        seq = ''.join(opponent_history)
    
    # Predict the opponent's next move based on the most frequent following move
    if seq in player.play_order:
        possible_moves = player.play_order[seq]
        prediction = max(possible_moves, key=possible_moves.get)
    else:
        prediction = random.choice(['R', 'P', 'S'])

    # The next move is the move that beats the predicted move
    guess = ideal_response[prediction]

    # Update the play_order dictionary with the new sequence
    if len(opponent_history) >= n:
        prev_seq = ''.join(opponent_history[-(n-1):])
        next_move = opponent_history[-1]

        if prev_seq in player.play_order:
            if next_move in player.play_order[prev_seq]:
                player.play_order[prev_seq][next_move] += 1
            else:
                player.play_order[prev_seq][next_move] = 1
        else:
            player.play_order[prev_seq] = {next_move: 1}

    return guess
