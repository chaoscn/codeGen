        public int $propertyName { get; set; }
        private void Update$propertyName()
        {
            try
            {
                if (_configurationDictionary.ContainsKey("$propertyKey"))
                {
                    $propertyName = Convert.ToInt32(_configurationDictionary["$propertyKey"]);
                    return;
                }
            }
            catch { }
            if ($propertyName == 0)
                $propertyName = $defaultValue;
        }