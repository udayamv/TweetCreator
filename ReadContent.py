from twython import Twython

# tweets the message
def tweet_status(message):
    print message
    twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
    twitter.update_status(status=message[:140])

def main():
    # read from a input text file with contents
    with open("Input.txt") as f:
        # fetch single line from file - line ends with \n character
        for line in f:
            # strip the white space characters
            line = line.strip()

            # If there is no full stop character in the line then it can be considered for tweeting
            if(".") not in line:
                # tweet the line
                tweet_status(line)
                #print "line: " + line
                continue

            # If there is a full stop character then split the line into sub lines with full stop as delimiter
            sub_line_arr = line.split(".")

            # loop through each subline
            for sub_line in sub_line_arr[:]:
                # if sub line is not empty
                if sub_line:
                    # strip any whitespace characters in the subline
                    sub_line = sub_line.strip()

                    # tweet the subline
                    tweet_status(sub_line)
                    #print "sub_line: "+sub_line

if __name__ == "__main__":
  main()