        public string $propertyName { get; set; }
        private void Update$propertyName()
        {
            try
            {
                if (_configurationDictionary.ContainsKey("$propertyKey"))
                {
                    $propertyName = _configurationDictionary["$propertyKey"];
                    return;
                }
            }
            catch { }
            if ($propertyName == null)
                $propertyName = "$defaultValue";
        }