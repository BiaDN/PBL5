        self.entry_txt_db = tk.StringVar()
        self.txt_db = tk.Entry(self, width=40, textvariable=self.entry_txt_db, font=("Arial", 11))
        self.txt_db.grid(column=1, row=15)

        self.btn_test = tk.Button(self, text="Test", command=self.btn_on_click, width=10)
        self.btn_test.grid(column=2, row=15)