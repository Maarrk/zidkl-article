line_interval = 0.1  # Data was logged at 10 Hz but fractions of seconds are missing

with open('example_2MG.txt', 'r') as file_in:
    with open('log_20141114T153149.csv', 'w') as file_out:
        _ = file_in.readline()  # Discard old header
        file_out.write('"time [s]";"load factor";"airspeed [km/h]"\n')

        second_repetitions = 0
        previous_second = 0
        for line_in in file_in:
            words = line_in.split()

            time_in = int(words[0])
            if time_in != previous_second:
                second_repetitions = 0

            time_out = float(time_in) + second_repetitions * line_interval
            file_out.write(f'{time_out:.1f};{words[1]};{words[3]}\n')

            second_repetitions += 1
            previous_second = time_in
