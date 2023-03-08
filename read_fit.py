import fitdecode
import pandas as pd


class Reader:

    def __init__(self, filename, log=None):
        self.filename = filename
        self.date = None
        self.fields = []
        self.frames = []
        self.df = None
        # set up logging
        self.log = log
        # read the file
        self._read()

    def __str__(self):
        return f"Workout reader\nDate: {self.date}\nFields: {self.fields}"

    ############################
    # Public methods
    ############################

    def disp_fields(self):
        self.log.info("List of fields: {}".format(self.fields))

    def disp_date(self):
        self.log.info("Date: {}-{}-{}".format(self.date.year, self.date.month, self.date.day))

    def get_data(self):
        return self.df

    ############################
    # Private methods
    ############################

    def _set_data(self, frame):
        """Set the data based on the first frame"""

        # get all available fields
        for field in frame.fields:
            if frame.get_value(field.name) is not None:
                self.fields.append(field.name)

        # get date
        self.date = frame.get_value('timestamp')

    def _build_df(self):
        """Build a pandas dataframe from the frames"""
        # make a pandas dataframe containing all the fields and the respective values arranged by timestamp
        self.df = pd.DataFrame(columns=self.fields)

        # for each frame append value of each filed in fields to the dataframe
        for frame in self.frames:
            row = []
            for field in self.fields:
                row.append(frame.get_value(field))
            self.df.loc[len(self.df)] = row

        # convert the timestamp to a datetime object
        self.df['timestamp'] = pd.to_datetime(self.df['timestamp'], unit='s')

        # set the timestamp as the index
        self.df.set_index('timestamp', inplace=True)

        # write to csv
        self.df.to_csv('sample/' + self.filename + '.csv')

    def _read(self):
        """Read the record file if needed convert it to a csv file"""

        # if the csv file already exists, read it and convert it to a dataframe
        # if not, read the fit file and convert it to a csv file
        try:
            self.df = pd.read_csv('sample/' + self.filename + '.csv', index_col=0, parse_dates=True)
            self.log.info("csv file found, converting to dataframe")
            # set the fields
            self.fields = self.df.columns.values.tolist()
            # set the date
            self.date = self.df.index[0]
            return
        except FileNotFoundError:
            self.log.info("No csv file found, converting fit file to csv")
            with fitdecode.FitReader('sample/' + self.filename + '.fit') as fit_file:
                set_data = True
                for frame in fit_file:
                    if isinstance(frame, fitdecode.records.FitDataMessage):
                        if frame.name == 'record':
                            if set_data:
                                self._set_data(frame)
                                set_data = False
                            self.frames.append(frame)

            self._build_df()

